from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, User
from .forms import CommentForm 

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
    comments = Comment.objects.filter(post = post_id)
    comment_form = CommentForm()
    return render(request, 'single_post.html', { 
      'post': post, 
      'user': request.user,
      'comments': comments,
      'comment_form': comment_form,
    })

@login_required
def add_comment(request, post_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post = Post.objects.get(id=post_id)
    new_comment.user = request.user
    new_comment.save()
  return redirect('detail', post_id=post_id)

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

class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ['text']

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  success_url = '/posts/'
  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    context['post_id'] = 9
    return context

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# def associate_comment(request, post_id, comment_id):
#   Post.objects.get(id=post_id).comments.add(comment_id)
#   return redirect('detail', post_id=post_id)

# def unassoc_comment(request, post_id, comment_id):
#   post_id = Comment.objects.get(id=comment_id).post_id
#   Post.objects.get(id=post_id).comments.remove(comment_id)
#   return redirect('post_detail', id=post_id)