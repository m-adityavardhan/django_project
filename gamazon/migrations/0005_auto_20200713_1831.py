# Generated by Django 3.0.8 on 2020-07-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamazon', '0004_remove_products_catag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pic',
            field=models.ImageField(upload_to='pics'),
        ),
    ]