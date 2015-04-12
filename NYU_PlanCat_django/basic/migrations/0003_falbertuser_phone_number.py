# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_auto_20150412_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='falbertuser',
            name='phone_number',
            field=models.CharField(default=datetime.date(2015, 4, 12), max_length=20, blank=True),
            preserve_default=False,
        ),
    ]
