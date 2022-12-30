"""Defines URL patterns for Blogs."""

from django.urls import path


from . import views

app_name = 'Blogs'

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page that shows all BlogPost.
    path('blogposts/', views.blogposts, name='blogposts'),
    # Page that shows single post
    #path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),
    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing a new post.
    path('edit_post/<int:blogpost_id>/', views.edit_post, name='edit_post'),
    
]
