# Generated by Django 4.0.2 on 2022-03-01 08:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at_name', models.DateTimeField(auto_created=datetime.datetime(2022, 3, 1, 8, 6, 9, 167971, tzinfo=utc), verbose_name='Created_at_verbose')),
                ('Task_name', models.CharField(max_length=100, verbose_name='Task_verbose')),
                ('Done_name', models.BooleanField(default=False, verbose_name='Done_verbose')),
            ],
        ),
    ]
