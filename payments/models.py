# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
import random


class Category(models.Model):
    title = models.CharField(u'Наименование услуги', max_length=50)
    slug = models.SlugField(u'Slug', unique=True)
    display = models.BooleanField(u'Включить/Отключить', default=True)
    img = models.ImageField(u'Ico', upload_to='media/image/uploads_category/')

    def __unicode__(self):
        return self.title


class Providers(models.Model):
    name = models.CharField(u'Имя провайдера', max_length=20)
    img = models.ImageField(u'Лого', upload_to='media/image/uploads_provider/')
    account = models.IntegerField(u'Л/С провайдера', unique=True, editable=False, blank=True)
    description = models.TextField(u'О провайдере')
    display = models.BooleanField(u'Включить/Отключить', default=False)
    category = models.ForeignKey(Category, verbose_name='Категорияы')
    manager = models.OneToOneField(User, verbose_name='Профайл провайдера', blank=True, null=True)

    def save(self):
        max_try = 100
        not_unique_number = True
        while not_unique_number:
            self.account = random.randint(100, 999)
            if max_try == 0:
                # Send email to admin
                break
            if Providers.objects.filter(account=self.account).count() == 0:
                not_unique_number = False
            max_try -= 1
        super(Providers, self).save()

    def __unicode__(self):
        return self.name
