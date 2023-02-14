from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from cloudinary.forms import cl_init_js_callbacks


def index(request):
    form = PostForm(request.POST, request.FILES)
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # if the form is valid
        if form.is_valid():
            # yes save
            form.save()
        # Redirect to home
            return HttpResponseRedirect('/')
        # no show Error
        else:
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts ,limit=20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # show
    return render(request, 'post.html',{'posts': posts, })


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post})


def likes(request, id):

    Likedtweet = Post.objects.get(id=id)
    new_value = Likedtweet.like_count +1
    Likedtweet.like_count = new_value
    Likedtweet.save()
    return HttpResponseRedirect('/')





