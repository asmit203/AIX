from django import forms
from .models import Feature

class PredictionForm(forms.ModelForm):
    class Meta:
        model=Feature
        fields='__all__'