# Generated by Django 2.1.7 on 2019-03-23 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20170717_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='faq.FAQCategory', verbose_name='Category'),
        ),
    ]