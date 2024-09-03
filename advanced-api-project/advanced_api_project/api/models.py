from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
from django.db import models

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Link to the author

    def __str__(self):
        return self.title

