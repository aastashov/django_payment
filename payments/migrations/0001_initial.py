# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('display', models.BooleanField(default=True, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c/\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c')),
                ('img', models.ImageField(upload_to=b'media/image/uploads_category/', verbose_name='Ico')),
            ],
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u0418\u043c\u044f \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440\u0430')),
                ('img', models.ImageField(upload_to=b'media/image/uploads_provider/', verbose_name='\u041b\u043e\u0433\u043e')),
                ('account', models.IntegerField(blank=True, editable=False, unique=True, verbose_name='\u041b/\u0421 \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440\u0430')),
                ('description', models.TextField(verbose_name='\u041e \u043f\u0440\u043e\u0432\u0430\u0439\u0434\u0435\u0440\u0435')),
                ('display', models.BooleanField(default=False, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c/\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.Category', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f\xd1\x8b')),
            ],
        ),
    ]
