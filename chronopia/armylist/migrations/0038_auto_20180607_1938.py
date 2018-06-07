# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armylist', '0037_auto_20180519_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='name',
            field=models.TextField(),
        ),
    ]
