# Generated by Django 2.2 on 2020-10-25 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0006_remove_readdetail_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='readdetail',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
