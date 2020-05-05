from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('feed/', views.feed, name='feed'),
  path('new-outdated/', views.new_post, name='new_post'),
  path('new/', views.PostCreate.as_view(), name="post_create")
]