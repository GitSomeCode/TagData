# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20150127_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_slug',
            field=models.SlugField(default=b'', unique=True),
            preserve_default=True,
        ),
    ]
