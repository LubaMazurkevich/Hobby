
from django.shortcuts import render
from films.models import Film
from library.models import Book


def book_film(request):
    books = Book.objects.all()
    films = Film.objects.all()
    context = {'books': books, 'films': films}

    return render(request, 'home.html',context)
