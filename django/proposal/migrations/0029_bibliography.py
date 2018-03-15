# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-27 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0028_auto_20170323_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='Determine processing order in output')),
                ('filename', models.CharField(help_text='Extension of the filename will be used to determine how to process this file.', max_length=64, verbose_name='Name of the bibliography file, including extension')),
                ('bibliography', models.TextField(help_text='Enter the actual bibliographic information, depending on the format you are using. ', verbose_name='Biboliographic information')),
            ],
            options={
                'abstract': False,
                'ordering': ['order'],
            },
        ),
    ]