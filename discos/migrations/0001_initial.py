# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-17 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta_disc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titol', models.CharField(max_length=120)),
                ('grup', models.CharField(max_length=120)),
                ('anny', models.DateField()),
                ('genere', models.CharField(max_length=50)),
                ('preu', models.IntegerField()),
                ('data_pujada', models.DateField()),
                ('venut', models.BooleanField(default=False, editable=False)),
                ('visible', models.BooleanField(default=True, editable=False)),
            ],
        ),
    ]
