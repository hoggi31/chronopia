# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0031_auto_20180514_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='magie',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
