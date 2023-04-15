# Generated by Django 4.1.7 on 2023-04-15 17:13

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tunipharmaApp', '0003_command_name_alter_command_date_cmd_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='command',
            options={'ordering': ['-date_cmd'], 'verbose_name': 'command'},
        ),
        migrations.AlterField(
            model_name='command',
            name='date_cmd',
            field=models.DateField(default=datetime.datetime(2023, 4, 15, 17, 12, 44, 360306, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='fabricationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='image/product_image'),
        ),
    ]