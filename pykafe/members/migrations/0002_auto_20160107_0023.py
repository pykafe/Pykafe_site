# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bio_text',
            field=models.TextField(help_text='Please write your bio text', max_length=1000),
        ),
        migrations.AlterField(
            model_name='member',
            name='job_title',
            field=models.CharField(help_text='Please write your job title', max_length=250),
        ),
    ]
