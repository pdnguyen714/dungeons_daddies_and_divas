from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def posts_index(request):
    return render(request, 'posts/index.html', { 'post': post})

def posts_detail(request, post_id):
    return render(request, 'posts/detail.html')

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text']

class PostDelete(DeleteView):
    model = Postsuccess_url = '/feed/'

