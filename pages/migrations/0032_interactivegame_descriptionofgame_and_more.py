# Generated by Django 4.2.11 on 2024-05-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_interactive_gameof'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactivegame',
            name='descriptionOfGame',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interactivegame',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='games/'),
        ),
    ]