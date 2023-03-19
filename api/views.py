from . import serializers
from django.forms import model_to_dict
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

    def get(self, request, id):
        posts_by_user = Post.objects.filter(user__id=id)
        serializer = serializers.UserPostsSerializer(posts_by_user, many=True)

        return Response(serializer.data)


class CommentByPost(APIView):

    def get(self, request, pk):
        comment_by_post = Comment.objects.filter(post__pk=pk)
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer





