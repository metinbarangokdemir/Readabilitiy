# Generated by Django 4.2.11 on 2024-05-31 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0043_alter_story_options_interactivegame_numberofplayer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_for_2p',
            name='second_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms_joined_2p', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room_for_3p',
            name='second_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms_joined_3p', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room_for_3p',
            name='third_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms_joined_3p_3rd', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room_for_4p',
            name='fourth_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms_joined_4p_4th', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room_for_4p',
            name='second_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms_joined_4p', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room_for_4p',
            name='third_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms_joined_4p_3rd', to=settings.AUTH_USER_MODEL),
        ),
    ]
