from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Author, Book


def author_list(request):
    a = Author.objects.all()
    return render(request, 'author_list.html', {
        'author_list': a,
        })

def author(request, pk):
    a = get_object_or_404(Author, pk=pk)
    book_list = Book.objects.filter(author=a)
    return render(request, 'author.html', {
        'author': a,
        'book_list': book_list
        })
    
def book(request, pk):
    b = get_object_or_404(Book, pk=pk)
    return render(request, 'book.html', {
        'book': b
        })
    
def user_profile(request, pk):
    userModel = get_user_model()
    u = get_object_or_404(userModel, id=pk)
    return render(request, 'profile.html', {
        'user': u,
        })
    