# Generated by Django 4.2.11 on 2024-05-05 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_interactivegame_descriptionofgame_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractiveContent',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='games/playing/')),
                ('partOf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.interactive')),
            ],
        ),
    ]
