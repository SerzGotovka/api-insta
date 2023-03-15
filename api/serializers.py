from rest_framework import serializers
from users.models import CustomUser
from insta.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    follows = serializers.SlugRelatedField(read_only=True, many=True, slug_field='username')

    class Meta:
        model = CustomUser
        fields = ['username', 'bio', 'photo', 'email', 'full_name', 'number_of_followers', 'number_of_follows',
                  'follows', 'is_active', 'date_joined', 'posts']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id',  'content', 'user', 'post', 'created')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    comments = serializers.SlugRelatedField(read_only=True, many=True, slug_field='content')

    class Meta:
        model = Post
        fields = ['id', 'title', 'photo', 'user', 'created', 'comments']

    def get_number_of_comments(self, obj):
        return Comment.objects.filter(post=obj).count()

