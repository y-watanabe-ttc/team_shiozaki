from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
from .forms import AbcForm

def index(req):
    posts = Post.objects.all()
    form = PostForm()
    context = {'posts': posts, 'form': form}
    return render(req, 'threads/index.html', context)

def add(req):
    form = PostForm(req.POST)
    form.save(commit=True)
    return HttpResponseRedirect(reverse('index'))

def add_quot(req, id=None):
    # print(req.POST)
    form = AbcForm(req.POST, initial = {'quote':id})
    form.save(commit=True)
    return HttpResponseRedirect(reverse('index'))

def delete(req, id=None):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

def abc(req, id=None):
    posts = Post.objects.all()
    form = AbcForm()
    # form = PostForm()
    context = {'posts': posts, 'form': form, "id": id}
    return render(req, 'threads/abc.html', context)