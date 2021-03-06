# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-15 12:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(help_text='Name of the company.', max_length=255)),
                ('description', models.TextField(help_text='Description of the company.')),
                ('address_line_1', models.CharField(help_text='Address line 1 of the company.', max_length=512)),
                ('address_line_2', models.CharField(help_text='Address line 2 of the company.', max_length=512)),
                ('state', models.CharField(help_text='State of the company.', max_length=12)),
                ('phone', models.CharField(help_text='Contact number of the company.', max_length=12)),
                ('gstin', models.CharField(help_text='GSTIN of the company.', max_length=30, unique=True)),
                ('tin', models.CharField(blank=True, help_text='TIN of the company.', max_length=30)),
                ('cin', models.CharField(blank=True, help_text='CIN of the company.', max_length=30)),
                ('bank_account', models.CharField(blank=True, help_text='Details of bank account of the company.', max_length=60)),
                ('invoice_terms_conditions', models.TextField(blank=True, help_text='Terms and Conditions that the company abide by.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='companies.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usercompany',
            unique_together=set([('user', 'company')]),
        ),
    ]
