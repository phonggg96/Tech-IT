# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20170901_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='discription',
        ),
    ]
