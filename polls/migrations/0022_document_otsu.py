# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20160711_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='otsu',
            field=models.BooleanField(default=False),
        ),
    ]
