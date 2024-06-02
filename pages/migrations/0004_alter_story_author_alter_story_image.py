# Generated by Django 4.2.11 on 2024-04-18 10:22

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_story_author_story_category_story_wordsize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.TextField(default='userName'),
        ),
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(default='stories/book.png', upload_to=pages.models.Story.upload_path),
        ),
    ]
