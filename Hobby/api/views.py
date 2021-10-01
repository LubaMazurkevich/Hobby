from django.shortcuts import render
# Create your views here.

# generics -коллекция представлений

from rest_framework import generics
from . import serializers
from library.models import Book
from films.models import Film
from serials.models import Tvserial


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class FilmList(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer


class FilmDetail(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer


class TvserialList(generics.ListAPIView):
    queryset = Tvserial.objects.all()
    serializer_class = serializers.TvserialSerializer


class TvserialDetail(generics.RetrieveAPIView):
    queryset = Tvserial.objects.all()
    serializer_class = serializers.TvserialSerializer