from django.forms import ModelForm, TextInput
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'email']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            })
        }
