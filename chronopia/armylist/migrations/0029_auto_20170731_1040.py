# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-31 08:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('armylist', '0028_spell_resistance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party_opponents',
            name='Troups_party',
        ),
        migrations.RemoveField(
            model_name='party_opponents',
            name='party',
        ),
        migrations.AddField(
            model_name='party',
            name='army_list',
            field=models.ManyToManyField(to='armylist.Army_Party', verbose_name='list of armies'),
        ),
        migrations.AddField(
            model_name='party',
            name='joueurs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Party_Opponents',
        ),
    ]
