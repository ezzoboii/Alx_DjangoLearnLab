from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
relationship_app/list_books.html", "Book.objects.all()
relationship_app/library_detail.html
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import permission_required", "relationship_app.can_add_book", "relationship_app.can_change_book", "relationship_app.can_delete_book
