from rest_framework import serializers
from users.models import CustomUser
from insta.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id',  'content', 'user', 'post', 'created')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'photo', 'text', 'user', 'created']

    def get_number_of_comments(self, obj):
        return Comment.objects.filter(post=obj).count()


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    follows = serializers.SlugRelatedField(read_only=True, many=True, slug_field='username')
    posts = PostSerializer(many=True, read_only=True)
    number_of_posts = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'bio', 'photo', 'email', 'full_name', 'number_of_followers', 'number_of_follows',
                  'number_of_posts', 'follows', 'is_active', 'date_joined', 'posts']

    def get_number_of_posts(self, obj):
        return Post.objects.filter(user=obj).count()


class UserPostsSerializer(serializers.ModelSerializer):
    number_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'photo', 'text', 'location', 'number_of_likes',
                  'number_of_comments', 'posted_on')

    def get_number_of_comments(self, obj):
        return Comment.objects.filter(post=obj).count()

