# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-21 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discos', '0003_auto_20170221_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta_disc',
            name='image',
            field=models.ImageField(blank=True, upload_to='discos'),
        ),
    ]