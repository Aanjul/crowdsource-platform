# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crowdsourcing', '0067_auto_20160112_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTurkAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_id', models.TextField(max_length=128)),
                ('worker_id', models.TextField(max_length=128)),
                ('status', models.IntegerField(choices=[(1, b'In Progress'), (2, b'Submitted'), (3, b'Accepted'), (4, b'Rejected'), (5, b'Returned'), (6, b'Skipped')], default=1)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MTurkHIT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit_id', models.TextField(max_length=256)),
                ('hit_type_id', models.TextField(default='', max_length=256)),
                ('hit_group_id', models.TextField(default='', max_length=128)),
                ('status', models.IntegerField(choices=[(1, 'Created'), (2, 'Completed'), (3, 'Done on Daemo'), (4, 'Forked')], default=1)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mturk_hits', to='crowdsourcing.Task')),
            ],
        ),
        migrations.AddField(
            model_name='mturkassignment',
            name='hit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mturk_assignments', to='mturk.MTurkHIT'),
        ),
        migrations.AddField(
            model_name='mturkassignment',
            name='task_worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mturk_assignments', to='crowdsourcing.TaskWorker'),
        ),
        migrations.AlterUniqueTogether(
            name='mturkhit',
            unique_together=set([('task', 'status')]),
        ),
    ]
