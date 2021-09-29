
from django.shortcuts import render
from films.models import Film
from library.models import Book
from serials.models import Tvserial


def book_film(request):
    books = Book.objects.all()
    films = Film.objects.all()
    serials = Tvserial.objects.all()
    context = {'books': books, 'films': films, 'serials': serials}

    return render(request, 'home.html',context)
