import self as self
from django import forms
from .models import photos

class ImageForm(forms.ModelForm):
    class Meta:
        model=photos
        fields=("title", "description", "location", "image")
