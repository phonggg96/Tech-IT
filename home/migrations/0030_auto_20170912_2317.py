# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20170912_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='tintuc',
            name='Decriptions',
            field=models.TextField(max_length=40000, null=True),
        ),
        migrations.AddField(
            model_name='tintuc',
            name='Image',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='tintuc',
            name='Is_HightLight',
            field=models.BooleanField(default=True),
        ),
    ]
