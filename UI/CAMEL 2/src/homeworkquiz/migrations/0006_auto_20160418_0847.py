# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkquiz', '0005_auto_20160404_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='multichoiceanswer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='singlechoiceanswer',
            name='correct',
            field=models.BooleanField(default=False),
        ),
    ]