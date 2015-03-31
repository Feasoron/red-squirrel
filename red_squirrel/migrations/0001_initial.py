# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ratio', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=1)),
                ('best_by', models.DateField(null=True, blank=True)),
                ('category', models.ManyToManyField(to='red_squirrel.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='food',
            name='location',
            field=models.ForeignKey(to='red_squirrel.StorageLocation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='unit',
            field=models.ForeignKey(to='red_squirrel.Unit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conversion',
            name='firstUnit',
            field=models.ForeignKey(related_name='first_unit', to='red_squirrel.Unit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='conversion',
            name='secondUnit',
            field=models.ForeignKey(related_name='second_unit', to='red_squirrel.Unit'),
            preserve_default=True,
        ),
    ]
