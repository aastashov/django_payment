# coding: utf-8
from django.db import models


class Categorie(models.Model):
    name = models.CharField(u'Наименование услуги', max_length=50)

    def __unicode__(self):
        return self.name


class Providers(models.Model):
    name = models.CharField(u'Имя провайдера', max_length=20)
    img = models.ImageField(u'Лого', upload_to='uploads_provider/')
    account = models.IntegerField(u'Л/С провайдера', unique=True)
    description = models.TextField(u'О провайдере')
    display = models.BooleanField(u'Включить/Отключить', default=False)
    categorie = models.ForeignKey(Categorie)

    def __unicode__(self):
        return self.name
