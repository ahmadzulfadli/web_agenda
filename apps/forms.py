from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = PostAgenda
        fields =['kegiatan', 'tempat', 'waktu', 'tanggal','file']

class AgendaForm(forms.ModelForm):
    class Meta:
        model = agenda
        fields =['r_kegiatan', 'r_tempat', 'r_waktu', 'r_tanggal']

class UserLogin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
