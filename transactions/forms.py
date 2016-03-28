# coding: utf-8
from django import forms
from models import Transactions


class TransactionForm(forms.ModelForm):
    class Meta():
        model = Transactions
        fields = {
            'amount',
            'props',
        }

        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Минимум 5сом'}),
            'props': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Лицевой счет'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 5:
            raise forms.ValidationError('Сумма должна быть не меньше 5 сом')
        return -amount
