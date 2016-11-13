# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseOperation', '0008_auto_20160907_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacherSet',
            field=models.ManyToManyField(null=True, to='databaseOperation.TeacherPointer'),
        ),
        migrations.AlterField(
            model_name='course',
            name='meta',
            field=models.TextField(blank=True, null=True),
        ),
    ]
