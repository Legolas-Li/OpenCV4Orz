# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20160710_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='prewitt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='roberts',
            field=models.BooleanField(default=False),
        ),
    ]
