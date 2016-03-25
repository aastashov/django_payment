# coding: utf-8
from django.db import models


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
    account = models.IntegerField(u'Л/С провайдера', unique=True)
    description = models.TextField(u'О провайдере')
    display = models.BooleanField(u'Включить/Отключить', default=False)
    category = models.ForeignKey(Category, verbose_name='Категорияы')

    def __unicode__(self):
        return self.name
