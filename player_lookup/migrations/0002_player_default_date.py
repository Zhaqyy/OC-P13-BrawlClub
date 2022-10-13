# Generated by Django 4.0.8 on 2022-10-13 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('player_lookup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='default_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 10, 13, 0, 0, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
