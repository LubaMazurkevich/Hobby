from django import forms
from .models import Book,BookSeries


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'genre', 'image')


class BookSeriesForm(forms.ModelForm):
    class Meta:
        model = BookSeries
        fields = ('title',)


