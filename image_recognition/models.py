from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
def user_directory_path(instance, filename, document_type):
    user_id = instance.user.id if instance.user else 'unknown'
    filename = f"user_{user_id}/{document_type}_{user_id}.png"
    return filename

def identification_directory_path(instance, filename):
    return user_directory_path(instance, filename, 'ID')

def curp_directory_path(instance, filename):
    return user_directory_path(instance, filename, 'CURP')

def rfc_directory_path(instance, filename):
    return user_directory_path(instance, filename, 'RFC')

def acta_directory_path(instance, filename):
    return user_directory_path(instance, filename, 'ACTA')

def seguro_directory_path(instance, filename):
    return user_directory_path(instance, filename, 'NSS')

class Documents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    identification = models.ImageField(upload_to=identification_directory_path, null=True)
    curp = models.ImageField(upload_to=curp_directory_path, null=True)
    rfc = models.ImageField(upload_to=rfc_directory_path, null=True)
    acta = models.ImageField(upload_to=acta_directory_path, null=True)
    seguro = models.ImageField(upload_to=seguro_directory_path, null=True)

    def __str__(self):
        return f'{self.user} docs'

