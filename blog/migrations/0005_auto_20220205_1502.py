# Generated by Django 3.2.6 on 2022-02-05 06:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220205_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 6, 2, 36, 540310, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 6, 2, 36, 540310, tzinfo=utc)),
        ),
    ]
