# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_timeline_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='registration',
            field=models.ForeignKey(blank=True, to='home.Registration', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registration',
            name='caption',
            field=models.CharField(default=None, max_length=180),
            preserve_default=False,
        ),
    ]
