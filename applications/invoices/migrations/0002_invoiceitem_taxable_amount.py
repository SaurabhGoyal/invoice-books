# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-15 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='taxable_amount',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Taxable amount of this item.', max_digits=16),
            preserve_default=False,
        ),
    ]
