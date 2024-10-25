from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
from .views import list_books

views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=
