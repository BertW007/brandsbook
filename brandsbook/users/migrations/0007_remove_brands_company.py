# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_brands'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brands',
            name='company',
        ),
    ]