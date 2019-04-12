# Generated by Django 2.1.7 on 2019-03-23 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('private_events', '0003_auto_20170717_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventreminder',
            name='notifyList',
            field=models.ManyToManyField(limit_choices_to={'is_staff': True}, to=settings.AUTH_USER_MODEL, verbose_name='Notification List'),
        ),
        migrations.AlterField(
            model_name='privateevent',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='private_events.PrivateEventCategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='privateevent',
            name='displayToGroup',
            field=models.ForeignKey(blank=True, help_text='If this is set, then only these users will see this event on their calendar.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='Display to group'),
        ),
        migrations.AlterField(
            model_name='privateevent',
            name='displayToUsers',
            field=models.ManyToManyField(blank=True, help_text='If this is set, then only chosen users will see this event on their calendar.', limit_choices_to={'is_staff': True}, to=settings.AUTH_USER_MODEL, verbose_name='Display to users'),
        ),
        migrations.AlterField(
            model_name='privateeventcategory',
            name='requiredGroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='Group required to add events to this category.'),
        ),
    ]