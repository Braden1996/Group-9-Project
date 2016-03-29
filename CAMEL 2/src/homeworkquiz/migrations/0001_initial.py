# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 22:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('latexbook', '0006_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='JaxAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('save_date', models.DateTimeField(auto_now=True)),
                ('submitted_date', models.DateTimeField(auto_now_add=True)),
                ('is_submitted', models.BooleanField(default=False)),
                ('node', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='latexbook.BookNode')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SingleChoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now=True)),
                ('save_date', models.DateTimeField(auto_now=True)),
                ('submitted_date', models.DateTimeField(auto_now=True)),
                ('is_submitted', models.BooleanField(default=False)),
                ('node', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='latexbook.BookNode')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
