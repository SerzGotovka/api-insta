from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='api-users'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='api-user'),
    path('posts/', views.PostList.as_view(), name='api-posts'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='api-post'),
    path('posts/user/<int:id>', views.PostsByUser.as_view(), name='api-user-posts'),

]