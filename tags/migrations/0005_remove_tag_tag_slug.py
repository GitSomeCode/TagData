# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0004_auto_20150127_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_slug',
        ),
    ]
