# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-11 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_auto_20160911_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='image_Link',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
