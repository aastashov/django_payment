# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from payments.models import Providers
from django.db.models.signals import post_save
from django.dispatch import receiver
import random


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь')
    first_name = models.CharField('Имя пользователя', max_length=100, blank=True)
    last_name = models.CharField('Фамилия пользователя', max_length=100, blank=True)
    account = models.IntegerField('Л/С пользователя', unique=True, editable=False, null=True)
    avatar = models.ImageField('Аватар пользователя', upload_to='media/image/uploads_avatar', blank=True)
    bookmarks = models.ManyToManyField(Providers, blank=True, verbose_name='Закладки')
    phone = models.CharField('Номер абонента', max_length=13, blank=True)

    def __unicode__(self):
        return self.user.username

    def get_balance(self):
        return sum([transaction.amount for transaction in self.transactions.all()])


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def created_profile(sender, instance, created, **kwargs):
    if created:
        max_try = 100
        not_unique_account = True
        while not_unique_account:
            account_gen = 1000 + random.randint(100, 999)
            if max_try == 0:
                # Send email to admin
                break
            if Profile.objects.filter(account=account_gen).count() == 0:
                not_unique_account = False
            max_try -= 1
        Profile.objects.create(
            user_id=instance.id,
            account=account_gen,
        )
