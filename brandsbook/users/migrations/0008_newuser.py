# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_brands_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=64)),
                ('nip', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=64)),
                ('post_code', models.CharField(max_length=6)),
                ('street', models.CharField(max_length=64)),
                ('nr', models.CharField(max_length=16)),
                ('phone', models.IntegerField(null=True)),
                ('brands', models.ManyToManyField(to='users.Brands')),
            ],
        ),
    ]
