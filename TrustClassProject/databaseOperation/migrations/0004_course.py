# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-06 05:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('databaseOperation', '0003_teacherpoiner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='waterCourse', max_length=255)),
                ('goodReviewCount', models.IntegerField(default=0)),
                ('neutralReviewCount', models.IntegerField(default=0)),
                ('badReviewCount', models.IntegerField(default=0)),
                ('meta', models.TextField(null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databaseOperation.School')),
            ],
        ),
    ]
