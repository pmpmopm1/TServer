# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170713_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]