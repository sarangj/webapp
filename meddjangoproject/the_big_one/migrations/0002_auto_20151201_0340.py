# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_big_one', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='date_entered',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date+time address entered'),
        ),
        migrations.AlterField(
            model_name='address',
            name='date_last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date+time last changed'),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is address actively being used'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
