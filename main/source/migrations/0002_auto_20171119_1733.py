# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='randnum',
            old_name='count_of_val',
            new_name='count_of_num',
        ),
    ]
