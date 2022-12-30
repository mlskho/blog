from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blogpost
from .forms import PostForm




# Create your views here.

def index(request):
    """The homepage for Blogs."""
    return render(request, 'Blogs/index.html')

def blogposts(request):
    """Show all Blogposts."""
    blogposts = Blogpost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'Blogs/blogposts.html', context)

#def blogpost(request, blogpost_id):
 #   """Show single post"""
#    blogpost = Blogpost.objects.get(id=blogpost_id)
 #   context = {'blogpost': blogpost}
#    return render(request, 'Blogs/blogpost.html', context)

@login_required   
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('Blogs:blogposts')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'Blogs/new_post.html', context)

@login_required   
def edit_post(request, blogpost_id):
    """Edit an existing post."""
    blogpost = Blogpost.objects.get(id=blogpost_id)
    if blogpost.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current post.
        form = PostForm(instance=blogpost)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blogs:blogposts')

    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'Blogs/edit_post.html', context)
        
                        
                        
            
