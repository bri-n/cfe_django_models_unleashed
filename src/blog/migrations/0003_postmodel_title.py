# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postmodel_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='New Title', max_length=240),
            preserve_default=False,
        ),
    ]