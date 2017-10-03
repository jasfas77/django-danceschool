# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-11 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20170909_0024'),
        ('private_lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructoravailabilityslot',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Room', verbose_name='Room'),
        ),
    ]