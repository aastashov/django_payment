# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.IntegerField(editable=False, unique=True, verbose_name='\u041b/\u0421 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f'),
        ),
    ]