from django import forms

from .models import Post

class PostForm(forms.ModelForm):
#this is my object constructor
    class Meta:
        model = Post
        fields = ('title', 'text',)
