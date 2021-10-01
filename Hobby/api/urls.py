from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('books_receive/', views.BookList.as_view()),
    path('books_receive/<int:pk>/', views.BookDetail.as_view()),
    path('films_receive/', views.FilmList.as_view()),
    path('films_receive/<int:pk>/', views.FilmDetail.as_view()),
    path('tv_serial_receive/', views.TvserialList.as_view()),
    path('tv_serial_receive/<int:pk>/', views.TvserialDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)