# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from payments.models import Providers


class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(u'Имя пользователя', max_length=100)
    last_name = models.CharField(u'Фамилия пользователя', max_length=100)
    account = models.IntegerField(u'Л/С пользователя', unique=True)
    balance = models.CharField(u'Баланс', max_length=250)
    avatar = models.ImageField(u'Аватар пользователя', upload_to='media/image/uploads_avatar', blank=True, null=True)
    bookmarks = models.ManyToManyField(Providers)

    def __unicode__(self):
        return self.user.username
