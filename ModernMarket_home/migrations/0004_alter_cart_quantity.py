# Generated by Django 4.1.3 on 2023-07-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModernMarket_home', '0003_wishlist_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]