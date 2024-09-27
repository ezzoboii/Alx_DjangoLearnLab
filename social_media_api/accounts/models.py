from django.contrib.auth.models import AbstractUser", "bio", "profile_picture", "followers", "models.ManyToManyField", "models.ImageField", "models.TextField
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username

