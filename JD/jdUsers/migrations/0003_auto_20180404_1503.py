# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jdUsers', '0002_auto_20180404_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='passwd',
            field=models.CharField(max_length=40, verbose_name='密码'),
        ),
    ]
