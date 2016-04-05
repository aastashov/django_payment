# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.IntegerField(verbose_name=b'\xd0\xa1\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='number',
            field=models.IntegerField(blank=True, editable=False, unique=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb7\xd0\xb0\xd0\xba\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='props',
            field=models.IntegerField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xb2\xd0\xb8\xd0\xb7\xd0\xb8\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payments.Providers', to_field=b'account', verbose_name=b'\xd0\x9b/\xd0\xa1 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='status',
            field=models.CharField(choices=[(b'success', b'\xd0\x9e\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbe'), (b'canceled', b'\xd0\x9e\xd1\x82\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xbe'), (b'revert', b'\xd0\x92\xd0\xbe\xd0\xb7\xd0\xb2\xd1\x80\xd0\xb0\xd1\x82'), (b'wait', b'\xd0\x9e\xd0\xb6\xd0\xb8\xd0\xb4\xd0\xb0\xd0\xb5\xd1\x82')], default=b'wait', max_length=50, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb7\xd0\xb0\xd0\xba\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='profiles.Profile', to_field=b'account', verbose_name=b'\xd0\x9b/\xd0\xa1 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f'),
        ),
    ]
