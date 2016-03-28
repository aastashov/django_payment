# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from payments.models import Providers
import random


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    first_name = models.CharField(u'Имя пользователя', max_length=100, blank=True)
    last_name = models.CharField(u'Фамилия пользователя', max_length=100, blank=True)
    account = models.IntegerField(u'Л/С пользователя', unique=True, editable=False)
    avatar = models.ImageField(u'Аватар пользователя', upload_to='media/image/uploads_avatar', blank=True)
    bookmarks = models.ManyToManyField(Providers, blank=True)
    phone = models.CharField(u'Номер абонента', max_length=13, blank=True)

    def save(self):
        max_try = 100
        not_unique_number = True
        while not_unique_number:
            self.account = 10000 + random.randint(100, 999)
            if max_try == 0:
                # Send email to admin
                break
            if Profile.objects.filter(account=self.account).count() == 0:
                not_unique_number = False
            max_try -= 1
        super(Profile, self).save()

    def __unicode__(self):
        return self.user.username
