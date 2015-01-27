# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tag_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_slug',
            field=models.SlugField(default=b''),
            preserve_default=True,
        ),
    ]
