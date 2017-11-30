# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 13:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('source', '0004_remove_randnum_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='randnum',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='randnum', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]