# coding: utf-8
from django import forms
from payment_messages.models import Message, Chat


class MessageForm(forms.ModelForm):
    class Meta():
        model = Message
        fields = [
            'text',
        ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
        }


class ChatForm(forms.ModelForm):
    class Meta():
        model = Chat
        fields = [
            'title',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема обращения'}),
        }
