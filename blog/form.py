from django import forms
from .models import BlogTable

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogTable
        fields = ['name', 'discription', 'image']
