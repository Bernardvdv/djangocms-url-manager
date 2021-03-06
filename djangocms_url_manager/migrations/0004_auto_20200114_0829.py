# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-14 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_url_manager', '0003_auto_20190524_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Modified'),
        ),
        migrations.AlterField(
            model_name='url',
            name='internal_name',
            field=models.CharField(default='', help_text='Provide internal name for URL objects for searching purpose', max_length=255, verbose_name='internal name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='urloverride',
            name='internal_name',
            field=models.CharField(default=' ', max_length=255, verbose_name='internal name'),
            preserve_default=False,
        ),
    ]
