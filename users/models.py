from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# from django.urls import reverse

from .managers import CustomUserManager
from django.utils import timezone


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.TextField(unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    follows = models.ManyToManyField(
        'CustomUser', blank=True, related_name='followers')
    facebook_username = models.TextField(blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def display_follows(self):
        return ", ".join([user.username for user in self.follows.all()])

    def number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def number_of_follows(self):
        return len([user for user in self.follows.all()]) if [user for user in self.follows.all()] else 0

    def number_of_followers(self):
        return len([user for user in self.followers.all()]) if [user for user in self.followers.all()] else 0
