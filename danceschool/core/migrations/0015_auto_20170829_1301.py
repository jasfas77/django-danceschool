# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170821_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporaryregistration',
            name='expirationDate',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='When a customer attempts to begin the registration process, the system looks for temporary registrations that are still in progress (with a future expiration date) to determine if there is space for them to register.', verbose_name='Expiration date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='temporaryregistration',
            name='email',
            field=models.CharField(max_length=200, null=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='temporaryregistration',
            name='firstName',
            field=models.CharField(max_length=100, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='temporaryregistration',
            name='lastName',
            field=models.CharField(max_length=100, null=True, verbose_name='Last name'),
        ),
    ]
