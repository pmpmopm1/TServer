# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_restaurant_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='osType',
            field=models.CharField(default='android', max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
