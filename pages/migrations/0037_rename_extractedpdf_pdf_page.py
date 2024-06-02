# Generated by Django 4.2.11 on 2024-05-28 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0036_delete_uploadedimage_profile_isemailverified'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExtractedPdf',
            new_name='Pdf',
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='pdfs/images/')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('partOf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.pdf')),
            ],
        ),
    ]
