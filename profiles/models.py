# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from payments.models import Providers


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    first_name = models.CharField(u'Имя пользователя', max_length=100, blank=True)
    last_name = models.CharField(u'Фамилия пользователя', max_length=100, blank=True)
    account = models.IntegerField(u'Л/С пользователя', unique=True, editable=False, null=True)
    avatar = models.ImageField(u'Аватар пользователя', upload_to='media/image/uploads_avatar', blank=True)
    bookmarks = models.ManyToManyField(Providers, blank=True)
    phone = models.CharField(u'Номер абонента', max_length=13, blank=True)

    def __unicode__(self):
        return self.user.username

    def get_balance(self):
        return sum([transaction.amount for transaction in self.transactions.all()])
