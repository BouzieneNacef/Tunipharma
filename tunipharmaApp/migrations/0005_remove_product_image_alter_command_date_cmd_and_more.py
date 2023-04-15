# Generated by Django 4.1.7 on 2023-04-15 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunipharmaApp', '0004_alter_command_options_alter_command_date_cmd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='command',
            name='date_cmd',
            field=models.DateField(default=datetime.datetime(2023, 4, 15, 17, 14, 27, 382084, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='fabricationDate',
            field=models.DateField(default=datetime.datetime(2023, 4, 15, 17, 14, 27, 382084, tzinfo=datetime.timezone.utc)),
        ),
    ]
