# Generated by Django 3.0.8 on 2020-07-13 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamazon', '0003_auto_20200712_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='catag',
        ),
    ]
