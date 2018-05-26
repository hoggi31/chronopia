# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0035_army_model_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='attack',
            name='portee',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
