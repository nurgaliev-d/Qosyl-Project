# Generated by Django 4.2.16 on 2024-12-10 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_chats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='chats',
        ),
        migrations.CreateModel(
            name='MyChats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chats', models.JSONField(default=dict)),
                ('frnd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_frnd', to=settings.AUTH_USER_MODEL)),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_me', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]