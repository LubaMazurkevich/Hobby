from time import timezone

from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookForm

# Create your views here.
from .models import Book
from django.shortcuts import redirect
from django.contrib.auth.models import User

def book_index(request):
    books=Book.objects.all()
    #запрос  вернет коллекцию всех книг
    context = {
        'books': books
    }
    return render(request, 'book_index.html', context)

def book_detail(request,pk):
    book=Book.objects.get(pk=pk) # извлекает проект с первичным ключом pk(ключ определенного проекта)
    context={
        'book': book
    }
    return render(request,'book_detail.html',context)


def books_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES) #POST-это публикация данных,все поля формы теперь в request.POST
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            book.author.add(User.objects.get_by_natural_key(request.user))
            return redirect('book_detail', pk=book.pk) # переадресация на страницу после добавления новой записи
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
