# Generated by Django 4.2.11 on 2024-04-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_remove_profile_userid_profile_id_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='UserId',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/default_profile.png', upload_to='profiles/<django.db.models.fields.BigAutoField>.jpg'),
        ),
    ]
