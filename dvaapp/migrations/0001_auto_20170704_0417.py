# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', 'custom_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_level', models.BooleanField(default=False)),
                ('start_frame_index', models.IntegerField()),
                ('end_frame_index', models.IntegerField()),
                ('metadata_text', models.TextField(default='')),
                ('metadata_json', models.TextField(default='')),
                ('end_frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_frame', to='dvaapp.Frame')),
            ],
        ),
        migrations.RemoveField(
            model_name='scene',
            name='end_frame',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='source',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='start_frame',
        ),
        migrations.RemoveField(
            model_name='scene',
            name='video',
        ),
        migrations.RemoveField(
            model_name='appliedlabel',
            name='scene',
        ),
        migrations.AlterField(
            model_name='region',
            name='region_type',
            field=models.CharField(choices=[('A', 'Annotation'), ('D', 'Detection'), ('P', 'Polygon'), ('S', 'Segmentation'), ('T', 'Transform')], max_length=1),
        ),
        migrations.DeleteModel(
            name='Scene',
        ),
        migrations.AddField(
            model_name='tube',
            name='end_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_region', to='dvaapp.Region'),
        ),
        migrations.AddField(
            model_name='tube',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='tube',
            name='start_frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_frame', to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='tube',
            name='start_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_region', to='dvaapp.Region'),
        ),
        migrations.AddField(
            model_name='tube',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='appliedlabel',
            name='tube',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Tube'),
        ),
    ]