from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='api-users'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='api-user'),
    path('posts/', views.PostList.as_view(), name='api-posts'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='api-post'),
    path('posts/user/<int:pk>', views.PostsByUser.as_view(), name='api-user-posts'),
    path('comments/', views.CommentList.as_view(), name='api-comments'),
    path('comments/post/<int:pk>/', views.CommentByPost.as_view(), name="api-comment-post"),
    path('comments/user/<int:pk>/', views.CommentByUser.as_view(), name="api-comment-user"),
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='api-comment'),
]
