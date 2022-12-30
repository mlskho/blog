from django import forms 

from .models import Blogpost

class PostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'text']
        labels = {'title': 'Blog Title:', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'placeholder': 'blog content...', 
        'cols': 100,}), }


