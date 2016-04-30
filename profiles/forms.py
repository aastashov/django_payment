# coding: utf-8
from models import Profile
from payments.models import Provider
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Отображаемое имя:', widget=forms.TextInput(
        attrs={
            'placeholder': 'Ivan',
            'class': 'form-control'
        }
    ))

    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(
        attrs={
            'placeholder': 'ivan123456',
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(label='Повторите пароль:', widget=forms.PasswordInput(
        attrs={
            'placeholder': 'ivan123456',
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'avatar',
            'phone',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '777171957'}),
            'avatar': forms.FileInput(),
        }


class ProviderForm(forms.ModelForm):
    class Meta():
        model = Provider
        fields = [
            'name',
            'description',
            'display',
            'category',
            'img',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'display': forms.CheckboxInput(attrs={'class': 'checkbox'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'img': forms.FileInput(),
        }


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Имя пользователя',
            'class': 'form-control'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Пароль',
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
