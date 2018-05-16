# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-07 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0004_auto_20161107_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='attaques',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='competences',
        ),
        migrations.AddField(
            model_name='attack',
            name='units',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attaques', to='armylist.Unit'),
        ),
        migrations.AddField(
            model_name='competence',
            name='units',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competences', to='armylist.Unit'),
        ),
    ]
