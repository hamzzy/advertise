# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-27 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappl', '0008_auto_20170927_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
