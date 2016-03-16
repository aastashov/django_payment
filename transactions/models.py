# coding: utf-8
from django.db import models

STATUS_SHOICES = (
    ('success', u'Оплачено'),
    ('canceled', u'Отменено'),
    ('revert', u'Возврат'),
)


class Transactions(models.Model):
    number = models.IntegerField(u'Номер транзакции', unique=True)
    account_user = models.CharField(max_length=100)
    account_provider = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_SHOICES)
    amount = models.IntegerField()
