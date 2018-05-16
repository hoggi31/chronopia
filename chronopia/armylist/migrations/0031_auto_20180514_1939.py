# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0030_auto_20170731_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='army_party',
            name='totalCost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
    ]
