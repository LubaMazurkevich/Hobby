from django import forms
from .models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'description', 'genre', 'image')

#
# class FilmLinkForm(forms.ModelForm):
#     class Meta:
#         model=FilmLink
#         fields=('link',)
