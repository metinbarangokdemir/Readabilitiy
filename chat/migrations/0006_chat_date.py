# Generated by Django 4.2.11 on 2024-05-30 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_messages_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
