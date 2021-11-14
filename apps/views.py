#============================================================================
#----------------------------IMPORT------------------------------------------
from django.db.models.fields import FilePathField
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import os

from .forms import PostForm, AgendaForm, UserLogin
from .models import PostAgenda, agenda
from apps.resource import AgendaResource
#----------------------------------------------------------------------------
#============================================================================

#============================================================================
#------------------------login dan registrasi--------------------------------
def registrasi(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserLogin()
        if request.method == 'POST':
            form = UserLogin(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Akun Berhasil Di buat untuk ' + user)
                return redirect('login')

    context = {
        'form':form,
    }
    return render(request,'user/registrasi.html',context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username atau Password salah')

    return render(request, 'user/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

#----------------------------------------------------------------------------
#============================================================================

#============================================================================
#----------------------------------CRUD--------------------------------------
@login_required(login_url='login')
def input(request):
    if request.method == "POST":
        kegiatan = PostForm(request.POST, request.FILES)
        if kegiatan.is_valid():
            kegiatan.save()
            messages.success(request, 'Data Berhasil Di Tambahkan')
            return redirect('tables')
    else:
        kegiatan = PostForm()

    context = {
        'kegiatan' : kegiatan,
    }
    return render(request, 'input.html', context)

@login_required(login_url='login')
def input_Agenda(request):
    if request.method == "POST":
        r_kegiatan = AgendaForm(request.POST)
        if r_kegiatan.is_valid():
            r_kegiatan.save()
            messages.success(request, 'Data Berhasil Di Tambahkan')
            return redirect('home')
    else:
        r_kegiatan = AgendaForm()

    context = {
        'r_kegiatan' : r_kegiatan,
    }
    return render(request, 'input_Agenda.html', context)
    
@login_required(login_url='login')
def ubah_data(request, id):
    model = PostAgenda.objects.get(id=id)
    form = PostForm(instance=model)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(model.file) > 0:
                os.remove(model.file.path)
            form = PostForm(request.POST, request.FILES, instance=model)
            if form.is_valid():
                form.save()
                messages.success(request, 'Data Berhasil Dirubah')
                return redirect('tables')
    context = {
        'form' : form,
        'model' : model,
        }

    return render(request, 'ubah_data.html', context)

@login_required(login_url='login')
def hapus(request, id):
    model = PostAgenda.objects.filter(id=id)

    if request.method == "POST":
        model.delete()
        if len(request.FILES) != 0:
            if len(model.file) > 0:
                os.remove(model.file.path)
        messages.success(request, 'Data Berhasil Dihapus')
        return redirect('tables')

    context = {
        'model': model,
    }
    return render(request, 'hapus.html', context)
#----------------------------------------------------------------------------
#============================================================================

#============================================================================
#---------------------------------TEMPLATES----------------------------------
@login_required(login_url='login')
def home(request):
    kegiatan = agenda.objects.all().order_by('-id')
    context = {
        'kegiatan' : kegiatan,
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def kalender(request):
    return render(request, 'kalender.html')

@login_required(login_url='login')
def tables(request):

    post = PostAgenda.objects.all().order_by('-id')
    context = {
        'post' : post,
    }
    return render(request, 'tables.html', context)

@login_required(login_url='login')
def lihat(request, id):

    post = PostAgenda.objects.get(id=id)
    context = {
        'post' : post,
    }
    return render(request, 'views_pdf.html', context)

@login_required(login_url='login')
def user(request):
    context = {

    }
    return render(request, 'account/user.html', context)
#----------------------------------------------------------------------------
#============================================================================

#============================================================================
#-----------------------------EXPORT EXEL------------------------------------
def export_xls(request):
    agenda = AgendaResource()
    dataset = agenda.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=agenda.xls'
    return response 
#----------------------------------------------------------------------------
#============================================================================




