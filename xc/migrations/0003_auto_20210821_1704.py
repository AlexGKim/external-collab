# Generated by Django 2.2.24 on 2021-08-22 00:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xc', '0002_auto_20210821_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='project_num',
            new_name='project',
        ),
        migrations.AddField(
            model_name='proposal',
            name='access',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='proposal',
            name='duration',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='granted_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='proposal',
            field=models.URLField(null=True),
        ),
    ]
