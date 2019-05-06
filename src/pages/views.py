from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SnippetForm, ContactForm


def index(request):
    return render(request, "index.html", {'title': 'Home'})

def list(request):
        return render(request, "list.html", {'title': 'blog'})

def contact(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you We will be in contact soon')
        return HttpResponseRedirect(reverse('home'))    
    form = SnippetForm()
    return render(request, "contact.html", {'form':form}, {'title': 'Contact'})

def project(request):
    return render(request, "project.html", {'title': 'projects'})

def terms(request):
    return render(request, "terms.html", {'title': 'Terms|Conditions'})

def privacy(request):
    return render(request, "privacy.html", {'title': 'Privacy Policy'})