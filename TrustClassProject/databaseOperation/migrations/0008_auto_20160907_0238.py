# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseOperation', '0007_auto_20160907_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='meta',
            field=models.TextField(blank=True, null=True),
        ),
    ]