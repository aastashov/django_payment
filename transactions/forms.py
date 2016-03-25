# coding: utf-8
from django import forms
from models import Transactions
import random


class TransactionForm(forms.ModelForm):
    class Meta():
        model = Transactions
        exclude = {
            'number',
        }

    def save(self, commit=True):
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
        transaction.number = int(number_gen)
        if commit:
            transaction.save()
        return transaction


# number = models.IntegerField(u'Номер транзакции', unique=True)
# user = models.ForeignKey(Profile, verbose_name='Л/С пользователя')
# provider = models.ForeignKey(Providers, verbose_name='Л/С провайдера')
# status = models.CharField('Статус транзакции', max_length=50, choices=STATUS_SHOICES)
# amount = models.IntegerField(u'Сумма платежа')
# create_at = models.DateTimeField(auto_now_add=True)
# props
