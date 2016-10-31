# coding: utf-8
from django import forms
from chat.models import Message


class MessageForm(forms.ModelForm):
    class Meta():
        model = Message
        fields = [
            'message',
        ]
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', 'autofocus': ''}),
        }
