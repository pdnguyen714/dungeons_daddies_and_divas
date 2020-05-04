from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('feed/', views.about, name='feed'),
  path('posts/<int:pk>/', views.posts_index, name="post_index")
]