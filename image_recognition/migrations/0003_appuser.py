# Generated by Django 4.2.5 on 2023-09-11 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_recognition', '0002_remove_documents_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('documents', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='image_recognition.documents')),
            ],
        ),
    ]
