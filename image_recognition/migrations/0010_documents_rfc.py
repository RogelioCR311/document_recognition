# Generated by Django 4.2.5 on 2023-10-08 18:55

from django.db import migrations, models
import image_recognition.models


class Migration(migrations.Migration):

    dependencies = [
        ('image_recognition', '0009_documents_curp_alter_documents_identification'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='rfc',
            field=models.ImageField(null=True, upload_to=image_recognition.models.rfc_directory_path),
        ),
    ]