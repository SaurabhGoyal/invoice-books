# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-17 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0002_auto_20170715_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Price of the item.', max_digits=12),
            preserve_default=False,
        ),
    ]