# Generated by Django 4.2.5 on 2023-09-11 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_recognition', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='user',
        ),
    ]
