from django.db import models
from users.models import CustomUser


class Post(models.Model):
    title = models.TextField(blank=True, max_length=100)
    photo = models.ImageField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='posts')
    text = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='liked_posts')

    def __str__(self):
        return self.title

    def display_likes(self):
        return ", ".join([user.username for user in self.likes.all()])

    def likesCount(self):
        return len([like for like in self.likes.all()]) if [like for like in self.likes.all()] else 0

    def number_of_likes(self):
        if self.likes.count():
            return self.likes.count()
        else:
            return 0

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    content = models.TextField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments', null=True)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.user

