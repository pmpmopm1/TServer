# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_restaruantmap'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RestaruantMap',
            new_name='RestaurantMap',
        ),
    ]
