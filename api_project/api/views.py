# api/views.py
from rest_framework import generics
from .models import Book  # Adjust the import based on your models location
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

