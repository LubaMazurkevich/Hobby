from rest_framework import serializers
from library.models import Book
from films.models import Film
from serials.models import Tvserial


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'genre', 'image']


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['title', 'description', 'genre', 'image']


class TvserialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tvserial
        fields = ['title', 'description', 'genre', 'image']