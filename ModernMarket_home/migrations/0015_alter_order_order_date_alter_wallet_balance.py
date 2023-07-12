# Generated by Django 4.1.3 on 2023-07-07 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModernMarket_home', '0014_rename_wallet_wallet_balance_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 7, 10, 2, 24, 108514, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=100000.0, max_digits=20),
        ),
    ]
