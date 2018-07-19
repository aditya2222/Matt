# Generated by Django 2.0.7 on 2018-07-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20180719_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spreadsheet',
            name='worksheet',
        ),
        migrations.AddField(
            model_name='spreadsheet',
            name='worksheet',
            field=models.ManyToManyField(blank=True, null=True, to='webapp.SpreadsheetModel'),
        ),
    ]