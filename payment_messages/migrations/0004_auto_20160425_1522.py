# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_messages', '0003_auto_20160425_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='status',
            field=models.BooleanField(choices=[(True, b'\xd0\x9e\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82'), (False, b'\xd0\x97\xd0\xb0\xd0\xba\xd1\x80\xd1\x8b\xd1\x82')], default=True, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd1\x87\xd0\xb0\xd1\x82\xd0\xb0'),
        ),
    ]
