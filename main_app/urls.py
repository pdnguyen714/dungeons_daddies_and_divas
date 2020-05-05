from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts_index, name='index'),
    path('posts/<int:post_id>', views.posts_detail, name='detail'),
    path('posts/create', views.PostCreate.as_view(), name="posts_create"),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name="posts_update"),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name="posts_delete"),
    path('comments/', views.CommentList.as_view(), name='comments_index'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comments_detail'),
    path('comments/create/', views.CommentCreate.as_view(), name='comments_create'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]