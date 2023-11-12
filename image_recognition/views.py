from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from .models import *
from .forms import *
from .ocr import *

# Create your views here.
def home(request):
    return redirect('signin')

def signin(request):
    if request.user.is_authenticated:
        return redirect('upload_docs')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('upload_docs')
        else:
            return render(request, 'pages-login.html', {
                'form': AuthenticationForm,
                'error': 'Email or password is incorrect'
            })

    return render(request, 'pages-login.html', {
        'form': AuthenticationForm
    })


def signup(request):
    if request.user.is_authenticated:
        return redirect('upload_docs')
    
    if request.method == 'GET':
        return render(request, 'pages-register.html', {
        'form': CustomUserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('upload_docs')
            except:
                return render(request, 'signup.html', {
                    'form': CustomUserCreationForm,
                    'error': 'Username already exist'
                })
            
        return render(request, 'signup.html', {
                    'form': CustomUserCreationForm,
                    'error': 'Passwords do not match'
                })

def signout(request):
    logout(request)
    return redirect('home')

@login_required
def upload_documents(request):
    if request.method == 'GET':
        idForm = UserIdForm(request.POST, request.FILES)
        curpForm = UserCurpForm(request.POST, request.FILES)
        rfcForm = UserRfcForm(request.POST, request.FILES)
        actaForm = UserActaForm(request.POST, request.FILES)
        seguroForm = UserSeguroForm(request.POST, request.FILES)

        return render(request, 'subir_docs.html', {'idForm': idForm, 'curpForm': curpForm, 'rfcForm': rfcForm, 'actaForm': actaForm, 'seguroForm': seguroForm})


def upload_id(request):
    if request.method == 'POST':
        idForm = UserIdForm(request.POST, request.FILES)
        if idForm.is_valid():
            user = request.user

            documents, created = Documents.objects.get_or_create(user=user)
            
            if documents.identification:
                documents.identification.delete()
            
            image_file = idForm.cleaned_data['identification']
            file_path = default_storage.save('temp_image.jpg', ContentFile(image_file.read()))
            imgURL = os.path.join(settings.BASE_DIR, f'media/{file_path}')

            result = readImage(imgURL, 'credential')

            if(result):
                documents.identification = idForm.cleaned_data['identification']
                documents.save()
                default_storage.delete(file_path)
            else:
                default_storage.delete(file_path)

            return redirect('upload_docs')
        
def upload_curp(request):
    if request.method == 'POST':
        curpForm = UserCurpForm(request.POST, request.FILES)
        if curpForm.is_valid():
            user = request.user

            documents, created = Documents.objects.get_or_create(user=user)
            
            if documents.curp:
                documents.curp.delete()

            image_file = curpForm.cleaned_data['curp']
            file_path = default_storage.save('temp_image.jpg', ContentFile(image_file.read()))
            imgURL = os.path.join(settings.BASE_DIR, f'media/{file_path}')

            result = readImage(imgURL, 'curp')
            
            if(result):
                documents.curp = curpForm.cleaned_data['curp']
                documents.save()
                default_storage.delete(file_path)
            else:
                default_storage.delete(file_path)

            return redirect('upload_docs')
        
def upload_rfc(request):
    if request.method == 'POST':
        rfcForm = UserRfcForm(request.POST, request.FILES)
        if rfcForm.is_valid():
            user = request.user

            documents, created = Documents.objects.get_or_create(user=user)
            
            if documents.rfc:
                documents.rfc.delete()

            image_file = rfcForm.cleaned_data['rfc']
            file_path = default_storage.save('temp_image.jpg', ContentFile(image_file.read()))
            imgURL = os.path.join(settings.BASE_DIR, f'media/{file_path}')

            result = readImage(imgURL, 'rfc')

            if(result):
                documents.rfc = rfcForm.cleaned_data['rfc']
                documents.save()
                default_storage.delete(file_path)
            else:
                default_storage.delete(file_path)

            return redirect('upload_docs')

def upload_acta(request):
    if request.method == 'POST':
        actaForm = UserActaForm(request.POST, request.FILES)
        if actaForm.is_valid():
            user = request.user

            documents, created = Documents.objects.get_or_create(user=user)
            
            if documents.acta:
                documents.acta.delete()

            image_file = actaForm.cleaned_data['acta']
            file_path = default_storage.save('temp_image.jpg', ContentFile(image_file.read()))
            imgURL = os.path.join(settings.BASE_DIR, f'media/{file_path}')

            result = readImage(imgURL, 'acta')

            if(result):
                documents.acta = actaForm.cleaned_data['acta']
                documents.save()
                default_storage.delete(file_path)
            else:
                default_storage.delete(file_path)

            return redirect('upload_docs')
        
def upload_seguro(request):
    if request.method == 'POST':
        seguroForm = UserSeguroForm(request.POST, request.FILES)
        if seguroForm.is_valid():
            user = request.user

            documents, created = Documents.objects.get_or_create(user=user)
            
            if documents.seguro:
                documents.seguro.delete()

            image_file = seguroForm.cleaned_data['seguro']
            file_path = default_storage.save('temp_image.jpg', ContentFile(image_file.read()))
            imgURL = os.path.join(settings.BASE_DIR, f'media/{file_path}')

            result = readImage(imgURL, 'nss')

            if(result):
                documents.seguro = seguroForm.cleaned_data['seguro']
                documents.save()
                default_storage.delete(file_path)
            else:
                default_storage.delete(file_path)

            return redirect('upload_docs')