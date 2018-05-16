# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-28 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0026_auto_20170601_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('lieu', models.CharField(max_length=100)),
                ('resume', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Party_Opponents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Troups_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armylist.Army_Party')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armylist.Party')),
            ],
        ),
        migrations.AddField(
            model_name='spell',
            name='action',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spell',
            name='portee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
