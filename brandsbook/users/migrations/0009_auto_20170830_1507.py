# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 15:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=64)),
                ('nip', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=64)),
                ('post_code', models.CharField(max_length=6)),
                ('street', models.CharField(max_length=64)),
                ('nr', models.CharField(max_length=16)),
                ('phone', models.IntegerField(null=True)),
                ('brands', models.ManyToManyField(to='users.Brands')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='brands',
        ),
        migrations.DeleteModel(
            name='NewUser',
        ),
    ]
