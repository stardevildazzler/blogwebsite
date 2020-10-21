from django.urls import path
from .import views
urlpatterns = [
    path('comment', views.blogcomment, name='blogcomment'),
    path('', views.blogposts, name='blogpost'),
    path('blogpage<slug>', views.blogpage, name='blogpage'),
    
]
