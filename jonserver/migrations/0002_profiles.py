# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jonserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('string', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=200)),
            ],
        ),
    ]
