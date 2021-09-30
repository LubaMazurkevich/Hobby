from time import timezone

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import BookForm

# Create your views here.
from .models import Book
from django.shortcuts import redirect
from django.contrib.auth.models import User


def book_index(request):
    books=Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book_index.html', context)


def book_detail(request,pk):
    book=Book.objects.get(pk=pk) 
    context={
        'book': book
    }
    return render(request,'book_detail.html', context)


def books_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES) 
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            book.author.add(User.objects.get_by_natural_key(request.user))
            return redirect('book_detail', pk=book.pk) 
    else:
        form = BookForm()
    return render(request, 'books.html', {'form': form})


def my_books(request):
    if request.user.is_authenticated:
        my_books = Book.objects.filter(author=request.user)
        context = {
            'my_books': my_books
        }

        return render(request, 'my_books.html', context)
    else:
        return HttpResponse('No authenticated,please login and then add books')


def books_add(request,pk):
    if request.user.is_authenticated:
        book = Book.objects.get(pk=pk)
        context = {
            'book': book
        }
        my_books = Book.objects.filter(author=request.user)
        context_1 = {
            'my_books': my_books
        }
        if book.author!=request.user:
            book.author.add(User.objects.get_by_natural_key(request.user))
            return render(request, 'my_books.html', context_1)
        else:
            return HttpResponse('Книга уже внесена в ваши книги!')
    else:
        return HttpResponse('Войдите в систему чтобы добавить книгу!')




def book_edit(request, pk):
    if request.user.is_superuser:
        book = get_object_or_404(Book, pk=pk)
        if request.method == "POST": # If the form has been submitted
                form = BookForm(request.POST, request.FILES, instance=book)
                if form.is_valid():
                    book = form.save(commit=False)
                    book.save()
                    book.author.add(User.objects.get_by_natural_key(request.user))
                    return redirect('book_detail', pk=book.pk)
        else:
            form = BookForm(instance=book)
        return render(request, 'book_edit.html', {'form': form})
    else:
        return HttpResponse('Only admin can edit books!')


def book_delete(request,pk):
    if request.user.is_superuser:
        books = Book.objects.all()
        context = {
            'books': books
        }
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return render(request, 'book_index.html', context)
        except Book.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")
    else:
        return HttpResponse('Only admin can delete books!')




