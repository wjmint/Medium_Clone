# Generated by Django 3.2.6 on 2021-11-13 05:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20211106_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 5, 18, 1, 368172, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 5, 18, 1, 367184, tzinfo=utc)),
        ),
    ]
