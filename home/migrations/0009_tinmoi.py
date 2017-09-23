# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170828_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tinmoi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=700)),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
    ]
