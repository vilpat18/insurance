# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 00:04
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import portal.fields.currency
import portal.fields.percentage


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0009_data_florida_counties'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performs', models.BooleanField(default=False)),
                ('work_percentage', portal.fields.percentage.PercentageField(default=0, validators=django.core.validators.MaxValueValidator(100))),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuickQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, ''), (10, ''), (20, ''), (30, ''), (40, ''), (50, ''), (60, '')], default=0)),
                ('surgery', models.PositiveSmallIntegerField(choices=[(0, 'None'), (50, 'Minor'), (100, 'Major')], default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('friendly_name', models.CharField(blank=True, max_length=50)),
                ('agency_name', models.CharField(max_length=50)),
                ('agent_name', models.CharField(max_length=30)),
                ('agent_email', models.EmailField(max_length=254)),
                ('insured_name', models.CharField(max_length=30)),
                ('prior_acts_effective_date', models.DateField(blank=True, null=True)),
                ('prior_acts_retroactive_date', models.DateField(blank=True, null=True)),
                ('board_actions_last_10_years', models.PositiveSmallIntegerField(default=0)),
                ('weekly_hours', models.PositiveSmallIntegerField(default=0)),
                ('weekly_patients', models.PositiveSmallIntegerField(default=0)),
                ('weekly_procedures', models.PositiveSmallIntegerField(default=0)),
                ('weekly_deliveries', models.PositiveSmallIntegerField(default=0)),
                ('weekly_reads', models.PositiveSmallIntegerField(default=0)),
                ('entity_coverage', models.BooleanField(default=False)),
                ('entity_note', models.TextField(blank=True)),
                ('professional_coverage', models.BooleanField(default=False)),
                ('professional_note', models.TextField(blank=True)),
                ('cosmetic_surgery', models.BooleanField(default=False)),
                ('cosmetic_elective_percentage', portal.fields.percentage.PercentageField(default=0, validators=django.core.validators.MaxValueValidator(100))),
                ('cosmetic_recon_percentage', portal.fields.percentage.PercentageField(default=0, validators=django.core.validators.MaxValueValidator(100))),
                ('claims_last_10_years', models.PositiveSmallIntegerField(default=0)),
                ('open_claims', models.PositiveSmallIntegerField(default=0)),
                ('closed_claims', models.PositiveSmallIntegerField(default=0)),
                ('current_carrier', models.CharField(blank=True, max_length=50)),
                ('expiring_premium', models.CharField(blank=True, max_length=10)),
                ('note', models.TextField(blank=True)),
                ('quoted_premium', portal.fields.currency.CurrencyField(blank=True, decimal_places=2, default=0, max_digits=8)),
                ('agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Agency')),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Agent')),
                ('bariatric_procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Procedure')),
                ('correctional_facilities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Procedure')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('deductible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Deductible')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('insured', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Insured')),
                ('laser_procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Procedure')),
                ('limit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Limit')),
                ('nursing_homes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Procedure')),
                ('primary_practice', models.ManyToManyField(related_name='primary_address', to='portal.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('practice_percentage', portal.fields.percentage.PercentageField(default=0, validators=django.core.validators.MaxValueValidator(100))),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StateCoverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_percentage', portal.fields.percentage.PercentageField(default=0, validators=django.core.validators.MaxValueValidator(100))),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.State')),
            ],
        ),
        migrations.AddField(
            model_name='quickquote',
            name='primary_speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Specialty'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='primary_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.StateCoverage'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='secondary_practice',
            field=models.ManyToManyField(related_name='secondary_address', to='portal.Address'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='secondary_speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Specialty'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='secondary_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.StateCoverage'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.State'),
        ),
        migrations.AddField(
            model_name='quickquote',
            name='telemedicine_procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Procedure'),
        ),
    ]
