# coding: utf-8
from django import forms
from payment_messages.models import Message


class MessageForm(forms.ModelForm):
    class Meta():
        model = Message
        fields = [
            'text',
        ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
        }
