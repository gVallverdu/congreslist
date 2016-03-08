from django import forms

from .models import Congress


class CongressForm(forms.ModelForm):

    class Meta:
        model = Congress
        fields = ('title', 'description', 'place')
