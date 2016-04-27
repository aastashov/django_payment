# coding: utf-8
from django.db import models
from payments.models import Providers
from profiles.models import Profile
import random

STATUS_SHOICES = (
    ('success', 'Оплачено'),
    ('canceled', 'Отменено'),
    ('revert', 'Запрос на возврат'),
    ('wait', 'Ожидает оплаты'),
)


class Transactions(models.Model):
    number = models.IntegerField(
        'Номер транзакции',
        unique=True,
        editable=False,
        blank=True
    )
    user = models.ForeignKey(
        Profile,
        verbose_name='Л/С пользователя',
        to_field='account',
        related_name='transactions',
    )
    provider = models.ForeignKey(
        Providers,
        verbose_name='Л/С провайдера',
        to_field='account',
    )
    status = models.CharField(
        'Статус транзакции',
        max_length=50,
        default='wait',
        choices=STATUS_SHOICES
    )
    amount = models.IntegerField('Сумма платежа')
    create_at = models.DateTimeField('Дата платежа', auto_now_add=True)
    props = models.IntegerField('Реквизит')

    def save(self):
        max_try = 100
        not_unique_number = True
        while not_unique_number:
            self.number = 1000 + random.randint(0, 9999)
            if max_try == 0:
                # Send email to admin
                break
            if Transactions.objects.filter(number=self.number).count() == 0:
                not_unique_number = False
            max_try -= 1
        super(Transactions, self).save()

    def __unicode__(self):
        return str(self.number)
