# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-22 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discos', '0004_oferta_disc_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta_disc',
            name='descripcio',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='oferta_disc',
            name='estat',
            field=models.CharField(default='', max_length=20),
        ),
    ]
