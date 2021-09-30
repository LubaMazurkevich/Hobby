from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView

from library.models import Book
from films.models import Film
from serials.models import Tvserial


# class SearchResultsView(ListView):
#     model = Book
#     template_name = 'home.html'
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Book.objects.filter(title__icontains=query)
#         return object_list


def search_results(request):
    query = request.GET.get('q')
    films = Film.objects.filter(title__icontains=query)
    books = Book.objects.filter(title__icontains=query)
    serials = Tvserial.objects.filter(title__icontains=query)
    context = {
        'films': films,
        'books': books,
        'serials': serials
    }
    return render(request, 'home.html', context)

