# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-05 12:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0005_auto_20170905_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]