from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('project/', views.project, name='project'),
    path('blog/', views.list, name='list'),
    path('Terms/', views.terms, name='terms'),
    path('Privacy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
]