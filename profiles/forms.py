# coding: utf-8
from models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import random
from transactions.models import Transactions


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={
            'placeholder': 'vanya',
            'class': 'form-control'
        }
    ))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'placeholder': u'pass123456',
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={
            'placeholder': u'pass123456',
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            max_try = 100
            not_unique_account = True
            while not_unique_account:
                account_gen = 1000 + random.randint(100, 999)
                if max_try == 0:
                    # Send email to admin
                    break
                if Profile.objects.filter(account=account_gen).count() == 0:
                    not_unique_account = False
                max_try -= 1
            Profile.objects.create(
                user_id=user.id,
                account=account_gen,
                balance=0,
            )
        return user


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


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={
            'placeholder': u'ivan',
            'class': 'form-control'
        }
    ))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'placeholder': u'pass123456',
            'class': 'form-control'
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class HistoryForm(forms.ModelForm):
    class Meta:
        model = Transactions
        exclude = (
            'number',
        )
