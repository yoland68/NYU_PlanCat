# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0003_falbertuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='rmp_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='time',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
