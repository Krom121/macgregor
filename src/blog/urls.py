from django.conf import settings
from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/',
     views.post_list, name='post_list_by_tag'),
    #path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),

] 