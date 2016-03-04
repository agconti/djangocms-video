# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_video_video', serialize=False, to='cms.CMSPlugin'),
        ),
    ]
