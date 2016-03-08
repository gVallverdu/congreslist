from django import forms

from .models import Congress


class CongressForm(forms.ModelForm):

    class Meta:
        model = Congress
        fields = ('title', 'description', 'place', 'start_date', 'end_date')
        labels = {
            "title": "Congress name",
            "description": "Scope",
            "start_date": "Start",
            "end_date": "end",
        }
