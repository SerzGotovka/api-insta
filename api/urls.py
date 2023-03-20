from django.urls import path
from . import views


urlpatterns = [

    # Все юзеры
    path('users/', views.UserList.as_view(), name='api-users'),

    # Детальный юзер
    path('user/<int:pk>', views.UserDetail.as_view(), name='api-user'),

    # Все посты
    path('posts/', views.PostList.as_view(), name='api-posts'),

    #Детальный пост
    path('post/<int:pk>', views.PostDetail.as_view(), name='api-post'),

    # Посты по юзеру
    path('posts/user/<int:pk>', views.PostsByUser.as_view(), name='api-user-posts'),

    # Все комментарии
    path('comments/', views.CommentList.as_view(), name='api-comments'),

    # Комментрарии по посту
    path('comments/post/<int:pk>/', views.CommentByPost.as_view(), name="api-comment-post"),

    # Комментрарии по юзеру
    path('comments/user/<int:pk>/', views.CommentByUser.as_view(), name="api-comment-user"),

    # Детальный комментарий
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='api-comment'),

    # Просмотр подписчиков по юзеру
    path('<slug:username>/get-followers/', views.GetFollowersView.as_view(), name='get-followers'),


    path('<slug:username>/follow/', views.FollowUserView.as_view(), name='follow-user'),

    # Просмотр наличия лайка по посту
    path('like/<int:post_id>/', views.LikeView.as_view(), name='like'),

    # """Просмотр поставленных лайков""",
    path('like/<int:post_id>/get-likers/', views.GetLikersView.as_view(), name='get-likers'),


]
