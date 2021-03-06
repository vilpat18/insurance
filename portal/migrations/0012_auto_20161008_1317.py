# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import portal.fields.currency


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20161001_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='DedLimitPremium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', portal.fields.currency.CurrencyField(blank=True, decimal_places=2, default=0, max_digits=8)),
                ('deductible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Deductible')),
                ('limit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Limit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='DeductibleLimit',
            new_name='DedLimitMultiplier',
        ),
        migrations.RemoveField(
            model_name='quickquote',
            name='deductible',
        ),
        migrations.RemoveField(
            model_name='quickquote',
            name='limit',
        ),
        migrations.RemoveField(
            model_name='quickquote',
            name='quoted_premium',
        ),
    ]
