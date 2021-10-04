from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_index, name='book_index'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('books_new/', views.books_new, name='books_new'),
    path('my_books/', views.my_books, name='my_books'),
    # path('book/<int:pk>/edit/', views.book_edit, name='book_edit'), #new
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('add/<int:pk>/', views.books_add, name='books_add'),
    path('add_book_to_series/<int:pk>/', views.add_book_to_series, name='add_book_to_series'),
    path('add_book_to_serie/<int:sk>/<int:bk>', views.add_book_to_serie, name='add_book_to_serie'),
    path('/seria_new/', views.create_serie_for_book, name='seria_new'),

]

