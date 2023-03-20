from . import serializers
from .serializers import FollowSerializer, PostSerializer, UserSerializer
from rest_framework import generics
from users.models import CustomUser
from insta.models import Post, Comment
from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostsByUser(APIView):

    def get(self, request, pk):
        posts_by_user = Post.objects.filter(user__pk=pk)
        serializer = serializers.PostSerializer(posts_by_user, many=True)

        return Response(serializer.data)


class CommentByPost(APIView):

    def get(self, request, pk):
        comment_by_post = Comment.objects.filter(post__pk=pk)
        serializer = serializers.CommentSerializer(comment_by_post, many=True)

        return Response(serializer.data)


class CommentByUser(APIView):

    def get(self, request, pk):
        comment_by_user = Comment.objects.filter(user__pk=pk)
        serializer = serializers.CommentSerializer(comment_by_user, many=True)

        return Response(serializer.data)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class GetFollowersView(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        queryset = CustomUser.objects.get(
            username=username).followers.all()
        return queryset


class LikeView(APIView):

    def get(self, request, format=None, post_id=None):
        post = Post.objects.get(pk=post_id)
        user = self.request.user
        if user.is_authenticated:
            if user in post.likes.all():
                like = False
                post.likes.remove(user)
            else:
                like = True
                post.likes.add(user)
        data = {
            'like': like
        }
        return Response(data)


class GetLikersView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        queryset = Post.objects.get(
            pk=post_id).likes.all()
        return queryset


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        queryset = Post.objects.all().filter(author__in=following_users)
        return queryset


class FollowUserView(APIView):

    def get(self, request, format=None, username=None):
        to_user = CustomUser.objects.get(username=username)
        from_user = self.request.user
        follow = None
        if from_user.is_authenticated:
            if from_user != to_user:
                if from_user in to_user.followers.all():
                    follow = False
                    from_user.following.remove(to_user)
                    to_user.followers.remove(from_user)
                else:
                    follow = True
                    from_user.following.add(to_user)
                    to_user.followers.add(from_user)
        data = {
            'follow': follow
        }
        return Response(data)
