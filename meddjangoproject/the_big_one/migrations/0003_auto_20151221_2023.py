# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_big_one', '0002_auto_20151201_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.ForeignKey(blank=True, null=True, to='the_big_one.Address'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='average_price',
            field=models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=2),
        ),
    ]
