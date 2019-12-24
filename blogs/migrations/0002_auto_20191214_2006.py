# Generated by Django 3.0 on 2019-12-14 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='admin', max_length=30),
        ),
        migrations.AddField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 12, 14, 20, 6, 17, 120250)),
        ),
    ]