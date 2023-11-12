# Generated by Django 4.2.5 on 2023-10-03 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image_recognition', '0006_remove_userinfo_documents_documents_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='curp',
        ),
        migrations.AlterField(
            model_name='documents',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]