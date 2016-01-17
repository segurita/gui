# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securities', '0003_auto_20160117_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialstatement',
            name='book_value_per_share',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='earnings_per_share',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='market_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='net_per_share_by_book_value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='net_working_capital',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='pe_ratio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='pe_times_price_by_book_value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialstatement',
            name='price_by_book_value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]