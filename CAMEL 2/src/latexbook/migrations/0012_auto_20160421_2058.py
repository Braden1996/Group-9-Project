# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 19:58
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('latexbook', '0011_auto_20160418_1207'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='booknode',
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]