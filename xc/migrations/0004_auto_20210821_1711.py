# Generated by Django 2.2.24 on 2021-08-22 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xc', '0003_auto_20210821_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='access',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='duration',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='proposal',
            field=models.URLField(blank=True, null=True),
        ),
    ]
