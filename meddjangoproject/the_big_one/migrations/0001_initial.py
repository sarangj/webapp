# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('street_number', models.CharField(max_length=15, blank=True)),
                ('street_name', models.CharField(max_length=200, blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'is address actively being used')),
                ('user_submitted', models.BooleanField(default=False)),
                ('date_entered', models.DateTimeField(auto_now_add=True, verbose_name=b'date+time address entered')),
                ('date_last_updated', models.DateTimeField(auto_now=True, verbose_name=b'date+time last changed')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=9)),
                ('average_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('address', models.ForeignKey(to='the_big_one.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialty_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(to='the_big_one.Specialty'),
        ),
    ]
