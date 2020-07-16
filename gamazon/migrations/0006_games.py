# Generated by Django 3.0.8 on 2020-07-16 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamazon', '0005_auto_20200713_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamazon.Products')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
