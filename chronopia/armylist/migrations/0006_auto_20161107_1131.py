# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-07 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0005_auto_20161107_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attack',
            name='units',
        ),
        migrations.AddField(
            model_name='attack',
            name='units',
            field=models.ManyToManyField(blank=True, null=True, related_name='attaques', to='armylist.Unit'),
        ),
        migrations.RemoveField(
            model_name='competence',
            name='units',
        ),
        migrations.AddField(
            model_name='competence',
            name='units',
            field=models.ManyToManyField(blank=True, null=True, related_name='competences', to='armylist.Unit'),
        ),
    ]
