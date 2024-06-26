# Generated by Django 4.1.3 on 2023-07-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_rating', models.DecimalField(decimal_places=1, max_digits=5)),
                ('p_description', models.CharField(max_length=500)),
                ('p_buycount', models.IntegerField()),
                ('p_brand', models.CharField(max_length=100)),
                ('p_category', models.CharField(max_length=100)),
                ('p_image', models.ImageField(upload_to='static/images/')),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
