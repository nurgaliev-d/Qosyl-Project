# Generated by Django 4.2.16 on 2024-12-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_chats_mychats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]