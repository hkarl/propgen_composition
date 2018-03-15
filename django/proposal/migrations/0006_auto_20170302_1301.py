# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-02 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0005_auto_20170302_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverablepartnertaskpm',
            name='task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='proposal.Task'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milestonepartnertaskpm',
            name='task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='proposal.Task'),
            preserve_default=False,
        ),
    ]
