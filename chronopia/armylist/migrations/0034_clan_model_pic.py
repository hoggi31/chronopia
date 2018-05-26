# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0033_auto_20180517_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='clan',
            name='model_pic',
            field=models.ImageField(null=True, upload_to='armylist/cards', blank=True),
        ),
    ]
