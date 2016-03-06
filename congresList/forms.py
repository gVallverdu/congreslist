from django import forms

from .models import Congre


class CongreForm(forms.ModelForm):

    class Meta:
        model = Congre
        fields = ('title', 'description', 'place')
