class CustomUser(AbstractUser):", "date_of_birth", "profile_photo
class CustomUserManager(BaseUserManager):", "create_user", "create_superuser
class Book(models.Model):", "can_create", "can_delete
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title

