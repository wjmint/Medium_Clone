# Generated by Django 3.1.7 on 2021-12-04 05:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0053_auto_20211127_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commets_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 5, 9, 37, 338985, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 5, 9, 37, 337987, tzinfo=utc)),
        ),
    ]
