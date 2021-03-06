# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-05 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0002_auto_20161105_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='TroupUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='army_party',
            name='totalCost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='army_party',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.RemoveField(
            model_name='army_party',
            name='unitList',
        ),
        migrations.AddField(
            model_name='troupunit',
            name='armyParty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armylist.Army_Party'),
        ),
        migrations.AddField(
            model_name='troupunit',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armylist.Unit'),
        ),
        migrations.AddField(
            model_name='army_party',
            name='unitList',
            field=models.ManyToManyField(through='armylist.TroupUnit', to='armylist.Unit'),
        ),
    ]
