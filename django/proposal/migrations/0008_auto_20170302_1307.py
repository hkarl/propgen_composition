# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-02 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0007_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.RemoveField(
            model_name='project',
            name='order',
        ),
    ]