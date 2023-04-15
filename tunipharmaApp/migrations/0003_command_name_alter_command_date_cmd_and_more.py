# Generated by Django 4.1.7 on 2023-04-15 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunipharmaApp', '0002_remove_client_clientproduct_delete_panier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='command',
            name='date_cmd',
            field=models.DateField(default=datetime.datetime(2023, 4, 15, 16, 59, 14, 825016, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='fabricationDate',
            field=models.DateField(default=datetime.datetime(2023, 4, 15, 16, 59, 14, 823974, tzinfo=datetime.timezone.utc)),
        ),
    ]