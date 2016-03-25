# coding: utf-8
from django import forms
from models import Transactions
import random


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

    def save(self, commit=True, u='', p=''):
        transaction = super(TransactionForm, self).save(commit=False)
        max_try = 100
        not_unique_number = True
        while not_unique_number:
            number_gen = 1000 + random.randint(100, 999)
            if max_try == 0:
                # Send email to admin
                break
            if Transactions.objects.filter(number=number_gen).count() == 0:
                not_unique_number = False
            max_try -= 1
        if commit:
            Transactions.objects.create(
                user_id=u,
                provider_id=p,
                number=number_gen,
                amount=transaction.amount,
                props=transaction.props
            )
        return transaction
