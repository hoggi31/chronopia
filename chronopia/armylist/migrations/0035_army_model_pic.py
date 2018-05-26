# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0034_clan_model_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='army',
            name='model_pic',
            field=models.ImageField(null=True, upload_to='armylist/cards', blank=True),
        ),
    ]
