# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=64)),
                ('nip', models.IntegerField()),
                ('city', models.CharField(max_length=64)),
                ('post_code', models.CharField(max_length=6)),
                ('street', models.CharField(max_length=64)),
                ('nr', models.CharField(max_length=16)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='firm',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Email', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='firm',
            name='password',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Password', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='firm',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Login', to=settings.AUTH_USER_MODEL),
        ),
    ]
