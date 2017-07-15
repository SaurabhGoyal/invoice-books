# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-15 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0001_initial'),
        ('taxes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('active', models.BooleanField(default=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxes', to='inventories.Item')),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='taxes.Tax')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='itemtax',
            unique_together=set([('item', 'tax')]),
        ),
    ]
