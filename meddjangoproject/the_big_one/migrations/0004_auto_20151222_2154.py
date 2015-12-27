# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('the_big_one', '0003_auto_20151221_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='date_entered',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 12, 22, 21, 53, 48, 391746, tzinfo=utc), verbose_name='date+time doctor entered'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='date_last_updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 12, 22, 21, 54, 0, 202160, tzinfo=utc), verbose_name='date+time last changed'),
            preserve_default=False,
        ),
    ]
