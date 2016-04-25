# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from payments.models import Providers

STATUS_CHOISES = (
    (True, 'Открыт'),
    (False, 'Закрыт'),
)


class Chat(models.Model):
    provider = models.ForeignKey(Providers, verbose_name='Получатель')
    token = models.IntegerField('Номер обращения', unique=True)
    title = models.CharField('Тема обращения', max_length=50)
    status = models.BooleanField('Статус чата', default=True, choices=STATUS_CHOISES)
    created_at = models.DateTimeField('Дата обращения', auto_now_add=True)

    def __unicode__(self):
        return self.title


class Message(models.Model):
    token = models.ForeignKey(Chat, verbose_name='Сообщения', to_field='token')
    sender = models.ForeignKey(User, verbose_name='Отправитель')
    text = models.TextField('Описание')
    created_at = models.DateTimeField('Дата сообщения', auto_now_add=True)

    def __unicode__(self):
        return str(self.sender)


class ClimeProvider(models.Model):
    provider = models.CharField('Компания', max_length=50)
    email = models.EmailField('Email')
    phone_number = models.CharField('Контактный номер', max_length=12)
    name = models.CharField('Контактное лицо', max_length=50)

    def __unicode__(self):
        return str(self.provider)
