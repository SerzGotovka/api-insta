from . import serializers
from rest_framework import generics
from users.models import CustomUser
from insta.models import Post, Comment
from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostsByUser(APIView):

    def get(self, request, id):
        posts_by_user = Post.objects.filter(user__id=id)
        serializer = serializers.PostSerializer(posts_by_user, many=True)

        return Response(serializer.data)


class CommentByPost(APIView):

    def get(self, request, id):
        comment_by_post = Comment.objects.filter(post__id=id)
        serializer = serializers.CommentSerializer(comment_by_post, many=True)

        return Response(serializer.data)


class CommentByUser(APIView):

    def get(self, request, id):
        comment_by_user = Comment.objects.filter(user__id=id)
        serializer = serializers.CommentSerializer(comment_by_user, many=True)

        return Response(serializer.data)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer





