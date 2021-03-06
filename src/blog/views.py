from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from taggit.models import Tag
from .models import Post, Comment
from .forms import CommentForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'

def post_list(request, tag_slug=None): 
    object_list = Post.published.all() 
    tag = None 

    if tag_slug: 
        tag = get_object_or_404(Tag, slug=tag_slug) 
        object_list = object_list.filter(tags__in=[tag]) 

    paginator = Paginator(object_list, 3) # 3 posts in each page 
    page = request.GET.get('page') 
    try: 
        posts = paginator.page(page) 
    except PageNotAnInteger: 
        # If page is not an integer deliver the first page 
        posts = paginator.page(1) 
    except EmptyPage: 
        # If page is out of range deliver last page of results 
        posts = paginator.page(paginator.num_pages) 
    return render(request, 'list.html', {'page': page, 
                                                   'posts': posts, 
                                                    'tag': tag, 'title': 'blog'})

def post_detail(request, year, month, day, post):
    comment_form = CommentForm()
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
   # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet          
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            messages.success(request, 'Your comment has been added successfully')
        return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()   
    
    return render(request,'detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form, 'title':'post'})
