# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20170912_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='tintuc',
            name='Content',
            field=models.TextField(max_length=40000, null=True),
        ),
        migrations.AlterField(
            model_name='tintuc',
            name='Decriptions',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tintuc',
            name='Is_HightLight',
            field=models.BooleanField(default=False),
        ),
    ]
