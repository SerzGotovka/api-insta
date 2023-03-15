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




