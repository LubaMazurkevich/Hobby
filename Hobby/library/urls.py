from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_index, name='book_index'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('books_new/', views.books_new, name='books_new'),
]

