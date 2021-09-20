from time import timezone

from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookForm

# Create your views here.
from .models import Book
from django.shortcuts import redirect

def book_index(request):
    books=Book.objects.all() #выполняем запрос,он позволяет создавать,извлекать объекты в базе данных
    #запрос возвращает коллекцию всех объектов,он вернет коллекцию всех книг
    context = {
        'books': books
    }
    return render(request, 'book_index.html', context)

def book_detail(request,pk):
    book=Book.objects.get(pk=pk) #делаем запрос,запрос извлекает проект с первичным ключом pk(ключ определенного проекта)
    context={
        'book': book
    }
    return render(request,'book_detail.html',context)


def books_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES) #POST-это публикация данных,все поля формы теперь в request.POST
        print(request.FILES)
        for i in form.data.items():
            print(i)
        if form.is_valid():
            # print("ter [ashete3")
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk) # переадресация на страницу после добавления новой записи
    else:
        form = BookForm()   #это когда хотим получить пустую форму??
    return render(request, 'books.html', {'form': form})


def my_books(request):
    my_books = Book.objects.filter(author=request.user)
    context = {
        'my_books': my_books
    }

    return render(request, 'my_books.html', context)

