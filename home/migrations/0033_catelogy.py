# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-13 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20170913_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catelogy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_cate', models.CharField(max_length=100)),
            ],
        ),
    ]
