# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-12 06:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_auto_20160911_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='social',
            name='in_Use',
        ),
    ]
