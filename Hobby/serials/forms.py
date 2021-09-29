from django import forms
from .models import Tvserial


class TvserialForm(forms.ModelForm):
    class Meta:
        model = Tvserial
        fields = ('title', 'description', 'genre', 'image')