# Generated by Django 3.2.3 on 2021-10-16 05:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20211016_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commets_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 16, 5, 34, 10, 667324, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 16, 5, 34, 10, 666340, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
