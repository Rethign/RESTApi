# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0006_randnum_rand_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='randnum',
            name='author',
        ),
    ]
