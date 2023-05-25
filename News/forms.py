from django import forms
from .models import Post


class NwForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'title', 'text']


class ArForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'title', 'text']