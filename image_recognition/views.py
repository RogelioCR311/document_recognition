from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import UserDocumentsForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request,'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('upload_docs')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exist'
                })
            
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Passwords do not match'
                })

def signout(request):
    logout(request)
    return redirect('home')

def upload_documents(request):
    if request.method == 'POST':
        form = UserDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user

            # Obtén o crea una instancia de Documents para el usuario actual
            documents, created = Documents.objects.get_or_create(user=user)

            # Elimina el documento de identificación anterior si existe
            if documents.identification:
                documents.identification.delete()

            # Elimina el documento CURP anterior si existe
            if documents.curp:
                documents.curp.delete()

            # Actualiza el campo 'identification' con la nueva imagen de identificación
            documents.identification = form.cleaned_data['identification']

            # Actualiza el campo 'curp' con la nueva imagen CURP
            documents.curp = form.cleaned_data['curp']

            documents.save()

            return redirect('upload_docs')
    else:
        form = UserDocumentsForm()
    return render(request, 'upload_docs.html', {'form': form})