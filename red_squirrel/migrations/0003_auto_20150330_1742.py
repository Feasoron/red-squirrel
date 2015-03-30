# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('red_squirrel', '0002_auto_20150330_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='best_by',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
