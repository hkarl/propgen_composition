# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-06 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0011_auto_20170303_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Include extensions like .tex or .md', max_length=64, verbose_name='Name of the produced file')),
                ('template', models.TextField(verbose_name='Actual template text (Jinja2)')),
                ('startpoint', models.BooleanField(default=False, help_text='Should this template be offered as a possible starting point from which to produce PDFs?', verbose_name='Start point')),
            ],
        ),
    ]