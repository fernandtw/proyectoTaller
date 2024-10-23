from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Perfil

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


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'avatar']



from django import forms
from .models import Perfil

from django import forms
from .models import Perfil

class EditarPerfilForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Perfil
        fields = ['bio', 'avatar',]
        widgets = {

            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super(EditarPerfilForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control'})
        if usuario:
            self.fields['email'].initial = usuario.email


