# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
