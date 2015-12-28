# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('the_big_one', '0002_auto_20151201_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorVisit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateTimeField(verbose_name=b'Date of Visit')),
                ('procedure', models.CharField(max_length=250, verbose_name=b'Procedure')),
                ('price', models.DecimalField(verbose_name=b'Price', max_digits=9, decimal_places=2)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=localflavor.us.models.USStateField(max_length=2, choices=[(b'AL', 'Alabama'), (b'AK', 'Alaska'), (b'AS', 'American Samoa'), (b'AZ', 'Arizona'), (b'AR', 'Arkansas'), (b'AA', 'Armed Forces Americas'), (b'AE', 'Armed Forces Europe'), (b'AP', 'Armed Forces Pacific'), (b'CA', 'California'), (b'CO', 'Colorado'), (b'CT', 'Connecticut'), (b'DE', 'Delaware'), (b'DC', 'District of Columbia'), (b'FL', 'Florida'), (b'GA', 'Georgia'), (b'GU', 'Guam'), (b'HI', 'Hawaii'), (b'ID', 'Idaho'), (b'IL', 'Illinois'), (b'IN', 'Indiana'), (b'IA', 'Iowa'), (b'KS', 'Kansas'), (b'KY', 'Kentucky'), (b'LA', 'Louisiana'), (b'ME', 'Maine'), (b'MD', 'Maryland'), (b'MA', 'Massachusetts'), (b'MI', 'Michigan'), (b'MN', 'Minnesota'), (b'MS', 'Mississippi'), (b'MO', 'Missouri'), (b'MT', 'Montana'), (b'NE', 'Nebraska'), (b'NV', 'Nevada'), (b'NH', 'New Hampshire'), (b'NJ', 'New Jersey'), (b'NM', 'New Mexico'), (b'NY', 'New York'), (b'NC', 'North Carolina'), (b'ND', 'North Dakota'), (b'MP', 'Northern Mariana Islands'), (b'OH', 'Ohio'), (b'OK', 'Oklahoma'), (b'OR', 'Oregon'), (b'PA', 'Pennsylvania'), (b'PR', 'Puerto Rico'), (b'RI', 'Rhode Island'), (b'SC', 'South Carolina'), (b'SD', 'South Dakota'), (b'TN', 'Tennessee'), (b'TX', 'Texas'), (b'UT', 'Utah'), (b'VT', 'Vermont'), (b'VI', 'Virgin Islands'), (b'VA', 'Virginia'), (b'WA', 'Washington'), (b'WV', 'West Virginia'), (b'WI', 'Wisconsin'), (b'WY', 'Wyoming')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(max_length=10),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(max_length=20),
        ),
        migrations.AddField(
            model_name='doctorvisit',
            name='address',
            field=models.ForeignKey(to='the_big_one.Address'),
        ),
        migrations.AddField(
            model_name='doctorvisit',
            name='doctor',
            field=models.ForeignKey(to='the_big_one.Doctor'),
        ),
    ]
