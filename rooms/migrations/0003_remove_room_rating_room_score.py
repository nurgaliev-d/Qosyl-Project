# Generated by Django 4.2.16 on 2024-12-06 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_room_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='rating',
        ),
        migrations.AddField(
            model_name='room',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]