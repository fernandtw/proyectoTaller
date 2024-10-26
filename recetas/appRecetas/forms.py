from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'ingredients', 'instructions', 'image', 'tabla', 'published', 'category']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 4}),
            'instructions': forms.Textarea(attrs={'rows': 4}),
        }
