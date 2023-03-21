from .models import *
from django.forms import ModelForm, DateTimeInput, TextInput, Textarea, DateInput
from django import forms
from django.contrib.auth.models import User
import re
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите адрес электронной почты',
        'type': 'email',
        'name': 'email',
        'id': 'id_email',
        }))

class UserSetPasswordForm(SetPasswordForm):
    error_messages = {
        "password_mismatch": ("The two password fields didn’t match."),
    }
    new_password1 = forms.CharField(
        label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите новый пароль',
        'type': 'password',
        'name': 'password1',
        'id': 'id_pass1',
        'strip': 'False',
        })
    )

    new_password2 = forms.CharField(
        label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль еще раз',
        'type': 'password',
        'name': 'password2',
        'id': 'id_pass2',
        })
    )

# Форма для профиля   
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', "id" : "username", "placeholder" : "Введите Имя Пользователя"}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', "id" : "email", "placeholder" : "Введите E-mail"}))

    class Meta:
        model = User
        fields = ['username', 'email']