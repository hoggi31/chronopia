# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-24 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0012_auto_20170524_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='tir',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
