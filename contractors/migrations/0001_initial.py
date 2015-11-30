# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('officialName', models.CharField(max_length=200)),
                ('edprou', models.PositiveIntegerField()),
                ('account', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mfo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('shortName', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='bankdetails',
            name='contractor',
            field=models.ManyToManyField(to='contractors.Contractor', related_name='bank'),
        ),
        migrations.AddField(
            model_name='accountingdetails',
            name='contactor',
            field=models.ForeignKey(to='contractors.Contractor', related_name='account'),
        ),
    ]
