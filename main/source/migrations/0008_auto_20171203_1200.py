# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 12:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0007_remove_randnum_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='randnum',
            old_name='max_val',
            new_name='dim',
        ),
    ]
