# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0036_attack_portee'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='cadence',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='attack',
            name='portee',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
