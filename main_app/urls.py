from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('feed/', views.posts_index, name='feed'),
  path('posts/<int:pk>/', views.posts_detail, name="post_index"),
  path('accounts/signup/', views.signup, name='signup'),
  path('posts/create', views.PostUpdate.as_view(), name="posts_create"),
  path('posts/<int:pk>', views.PostDelete.as_view(), name="posts_delete")
]