# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pubticker',
            fields=[
                ('pair_id', models.CharField(max_length=20)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('import_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mid', models.DecimalField(max_digits=30, decimal_places=10)),
                ('bid', models.DecimalField(max_digits=30, decimal_places=10)),
                ('ask', models.DecimalField(max_digits=30, decimal_places=10)),
                ('last_price', models.DecimalField(max_digits=30, decimal_places=10)),
                ('low', models.DecimalField(max_digits=30, decimal_places=10)),
                ('high', models.DecimalField(max_digits=30, decimal_places=10)),
                ('volume', models.DecimalField(max_digits=30, decimal_places=10)),
                ('timestamp', models.DecimalField(max_digits=30, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('close_price', models.DecimalField(max_digits=30, decimal_places=10)),
                ('close_return', models.DecimalField(max_digits=30, decimal_places=10)),
                ('pubticker', models.ForeignKey(to='trader.Pubticker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
