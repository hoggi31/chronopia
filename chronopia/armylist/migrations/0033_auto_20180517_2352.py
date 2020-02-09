# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0032_unit_magie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='unit',
            name='bouclier',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='clan',
            field=models.ForeignKey(related_name='unitList', blank=True, to='armylist.Clan', null=True),
        ),
    ]