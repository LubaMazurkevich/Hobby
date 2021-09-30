from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_index, name='book_index'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('books_new/', views.books_new, name='books_new'),
    path('my_books/', views.my_books, name='my_books'),
    # path('book/<int:pk>/edit/', views.book_edit, name='book_edit'), #new
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete')
]

