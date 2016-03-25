# coding: utf-8
from django.db import models
from payments.models import Providers
from profiles.models import Profile

STATUS_SHOICES = (
    ('success', u'Оплачено'),
    ('canceled', u'Отменено'),
    ('revert', u'Возврат'),
)


class Transactions(models.Model):
    number = models.IntegerField(u'Номер транзакции', unique=True)
    user = models.ForeignKey(Profile, verbose_name='Л/С пользователя', to_field='account')
    provider = models.ForeignKey(Providers, verbose_name='Л/С провайдера', to_field='account')
    status = models.CharField('Статус транзакции', max_length=50, choices=STATUS_SHOICES)
    amount = models.IntegerField(u'Сумма платежа')
    create_at = models.DateTimeField(auto_now_add=True)
    props = models.IntegerField(u'Реквизит')
