# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-09 04:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databaseOperation', '0019_course_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Icon',
            new_name='iconType',
        ),
    ]