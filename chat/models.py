# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save, pre_init
# from django.dispatch import receiver


class Chat(models.Model):
    title = models.CharField('Тема', max_length=50)
    users = models.ManyToManyField(User, verbose_name='Участники чата')
    status = models.BooleanField('Отображение чата', default=True)

    def __unicode__(self):
        return unicode(self.title) or u''


class Message(models.Model):
    chat = models.ForeignKey(Chat)
    sender = models.ForeignKey(User)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.chat) or u''


class ClimeProvider(models.Model):
    provider = models.CharField('Компания', max_length=50)
    email = models.EmailField('Email')
    phone_number = models.CharField('Контактный номер', max_length=12)
    name = models.CharField('Контактное лицо', max_length=50)

    def __unicode__(self):
        return unicode(self.provider) or u''


# @receiver(post_save, sender=Message, dispatch_uid="new_message")
# def created_new_message(sender, instance, created, **kwargs):
#     if created:
#         instance.chat.new_message += 1
#         instance.chat.save()


# @receiver(post_init, sender=Message, dispatch_uid="view_message")
# def view_message(sender, instance, created, **kwargs):
#     if created:
#         instance.chat.new_message = 0
#         instance.chat.save()
