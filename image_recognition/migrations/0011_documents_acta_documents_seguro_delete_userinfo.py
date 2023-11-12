# Generated by Django 4.2.5 on 2023-11-11 22:05

from django.db import migrations, models
import image_recognition.models


class Migration(migrations.Migration):

    dependencies = [
        ('image_recognition', '0010_documents_rfc'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='acta',
            field=models.ImageField(null=True, upload_to=image_recognition.models.acta_directory_path),
        ),
        migrations.AddField(
            model_name='documents',
            name='seguro',
            field=models.ImageField(null=True, upload_to=image_recognition.models.seguro_directory_path),
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]