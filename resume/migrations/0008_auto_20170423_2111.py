# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 02:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_language_fakecolumn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='fakeColumn',
        ),
        # migrations.RemoveField(
        #     model_name='language',
        #     name='id',
        # ),
        migrations.AddField(
            model_name='language',
            name='technology',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='resume.Technology'),
        ),
    ]
