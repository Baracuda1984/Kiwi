# Generated by Django 2.0.3 on 2018-03-13 21:35
from datetime import timedelta
from django.db import migrations, models


def forward(apps, schema_editor):
    TestRun = apps.get_model('testruns', 'TestRun')

    for tr in TestRun.objects.all():
        tr.estimated_time_new = timedelta(seconds=tr.estimated_time)
        tr.save()


def reverse(apps, schema_editor):
    TestRun = apps.get_model('testruns', 'TestRun')

    for tr in TestRun.objects.all():
        tr.estimated_time = tr.estimated_time_new.total_seconds()
        tr.save()


class Migration(migrations.Migration):

    dependencies = [
        ('testruns', '0009_rename_testtag'),
    ]

    operations = [
        # add a timedelta field
        migrations.AddField(
            model_name='testrun',
            name='estimated_time_new',
            field=models.DurationField(default=timedelta(0)),
        ),
        # migrate the values
        migrations.RunPython(forward, reverse),
        # remove the integer field
        migrations.RemoveField(
            model_name='testrun',
            name='estimated_time',
        ),
        # rename the new field to the old name
        migrations.RenameField(
            model_name='testrun',
            old_name='estimated_time_new',
            new_name='estimated_time',
        ),
    ]