# Generated by Django 3.1.7 on 2021-11-27 04:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0052_auto_20211127_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commets_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 4, 51, 6, 255311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 4, 51, 6, 255311, tzinfo=utc)),
        ),
    ]
