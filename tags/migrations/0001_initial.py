# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metric', models.FloatField(default=0.0)),
                ('tag_from', models.ForeignKey(related_name='tag_from', to='tags.Tag')),
                ('tag_to', models.ForeignKey(related_name='tag_to', to='tags.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tagrelation',
            unique_together=set([('tag_to', 'tag_from')]),
        ),
        migrations.AddField(
            model_name='tag',
            name='relation',
            field=models.ManyToManyField(to='tags.Tag', through='tags.TagRelation'),
            preserve_default=True,
        ),
    ]
