# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0037_auto_20160713_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='average_blur',
            field=models.BooleanField(default=False),
        ),
    ]
