# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-23 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0025_auto_20170319_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='_requested_contribution',
            field=models.FloatField(default=-1.0, help_text='Default negative value means requested contribution equals maximum contribution.Only fill in this field if you want to request less money than the maximum allows you to do. This is usually not recommended.', verbose_name='Requested contribution'),
        ),
        migrations.AddField(
            model_name='partner',
            name='finanical_support_3rd',
            field=models.FloatField(default=0.0, verbose_name='Financial support for 3rd parties'),
        ),
        migrations.AddField(
            model_name='partner',
            name='finanical_support_3rd_explanation',
            field=markdownx.models.MarkdownxField(blank=True, help_text='Provide explanation', verbose_name='Explanation of financial support to 3rd parties'),
        ),
        migrations.AddField(
            model_name='partner',
            name='inkind_contributions',
            field=models.FloatField(default=0.0, verbose_name='In-kind contributions'),
        ),
        migrations.AddField(
            model_name='partner',
            name='inkind_contributions_explanations',
            field=markdownx.models.MarkdownxField(blank=True, verbose_name='Explanation of in-kind contributions'),
        ),
        migrations.AddField(
            model_name='partner',
            name='other_direct_cost',
            field=models.FloatField(default=-1.0, help_text='Corresponds to Col. B. If negative, the value is computed from other fields!', verbose_name='Other direct cost'),
        ),
        migrations.AddField(
            model_name='partner',
            name='other_direct_cost_explanation',
            field=markdownx.models.MarkdownxField(blank=True, help_text='Provide explanation for other direct cost if they exceed 15% of the personnel cost (as per guidelines).', verbose_name='Explanation for other direct cost'),
        ),
        migrations.AddField(
            model_name='partner',
            name='pic',
            field=models.CharField(default='', help_text='Participant Identification Code', max_length=16, verbose_name='PIC'),
        ),
        migrations.AddField(
            model_name='partner',
            name='reimbursement_rate',
            field=models.FloatField(default=100.0, help_text='Make sure the reimbursement rate is consistent with the partner type', verbose_name='Reimbursement rate'),
        ),
        migrations.AddField(
            model_name='partner',
            name='special_uni_cost',
            field=models.FloatField(default=0.0, verbose_name='Special unit cost'),
        ),
        migrations.AddField(
            model_name='partner',
            name='special_uni_cost_explanation',
            field=markdownx.models.MarkdownxField(blank=True, verbose_name='Explanation of special unit cost'),
        ),
        migrations.AddField(
            model_name='partner',
            name='subcontract_cost',
            field=models.FloatField(default=0.0, help_text='Total cost of all subcontracting done by this partner', verbose_name='Subcontractig cost'),
        ),
        migrations.AddField(
            model_name='partner',
            name='subcontract_cost_explanation',
            field=markdownx.models.MarkdownxField(blank=True, help_text='Usually, explanation for subcontracting is necessary', verbose_name='Explanation for subcontracts'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='PMcost',
            field=models.FloatField(default=0.0, help_text='This relates to the Direct Personnel Cost (Col. A) via the number of personmonths', verbose_name='Person month cost'),
        ),
    ]
