# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170830_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='company',
            field=models.ManyToManyField(to='users.Detail'),
        ),
    ]
