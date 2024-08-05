# Generated by Django 5.0.6 on 2024-07-30 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_chatsession_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='chat_session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chatsession_id', to='chat.chatsession'),
        ),
    ]
