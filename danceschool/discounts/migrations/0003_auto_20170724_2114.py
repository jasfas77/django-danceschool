# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-24 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0002_auto_20170717_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcombo',
            name='discountType',
            field=models.CharField(choices=[('F', 'Exact Specified Price'), ('D', 'Dollar Discount from Regular Price'), ('P', 'Percentage Discount from Regular Price'), ('A', 'Free Add-on Item (Can be combined with other discounts)')], default='D', help_text="Is this a flat price, a dollar amount discount, a 'percentage off' discount, or a free add-on?", max_length=1, verbose_name='Discount type'),
        ),
    ]