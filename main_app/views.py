from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, Profile

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', { 'posts': posts })

@login_required
def single_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'single_post.html', { 
      'post': post, 
      'user': request.user,
    })

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'

class CommentList(LoginRequiredMixin, ListView):
  model = Comment

class CommentDetail(LoginRequiredMixin, DetailView):
  model = Comment

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
   

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ['text']

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  success_url = '/comments/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)