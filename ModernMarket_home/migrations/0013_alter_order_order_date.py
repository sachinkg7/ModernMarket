# Generated by Django 4.1.3 on 2023-07-07 09:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModernMarket_home', '0012_alter_order_order_date_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 7, 9, 55, 19, 558805, tzinfo=datetime.timezone.utc)),
        ),
    ]