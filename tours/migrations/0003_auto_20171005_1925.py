# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-05 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20171005_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='period',
            name='high',
            field=models.DecimalField(decimal_places=2, default=90, max_digits=10),
        ),
        migrations.AddField(
            model_name='period',
            name='low',
            field=models.DecimalField(decimal_places=2, default=60, max_digits=10),
        ),
        migrations.AddField(
            model_name='period',
            name='medium',
            field=models.DecimalField(decimal_places=2, default=75, max_digits=10),
        ),
        migrations.AlterField(
            model_name='period',
            name='high_period',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='period',
            name='low_period',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='period',
            name='medium_period',
            field=models.BooleanField(default=False),
        ),
    ]