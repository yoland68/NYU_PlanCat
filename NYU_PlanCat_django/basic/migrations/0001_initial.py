# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_id', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=30)),
                ('period', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('open', models.BooleanField(default=None)),
                ('format', models.CharField(max_length=20)),
                ('professor', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('rmp_link', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_id', models.CharField(unique=True, max_length=30)),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('offering', models.BooleanField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FalbertUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('net_id', models.CharField(max_length=20, blank=True)),
                ('current_class_schedule_confirmed', models.BooleanField(default=False)),
                ('courses_taken', models.ManyToManyField(related_name=b'courses', to='basic.Class')),
                ('current_class_schedule', models.ManyToManyField(related_name=b'students', to='basic.Class')),
                ('interested_classes', models.ManyToManyField(related_name=b'class_followers', to='basic.Class')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('major_id', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('requirements', models.ManyToManyField(related_name=b'+', to='basic.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='falbertuser',
            name='major',
            field=models.ManyToManyField(related_name=b'students', to='basic.Major'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='parent_course',
            field=models.ForeignKey(to='basic.Course'),
            preserve_default=True,
        ),
    ]
