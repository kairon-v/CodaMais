# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_auto_20170406_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]