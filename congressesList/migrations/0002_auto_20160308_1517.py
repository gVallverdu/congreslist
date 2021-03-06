# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-08 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('congressesList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congress',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='congress',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='congress',
            name='place',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='congress',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
