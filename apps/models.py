from django.db import models
from django.db.models.deletion import CASCADE
import django.db.models.fields
import datetime

class PostAgenda(models.Model):
    kegiatan = models.CharField(max_length=50)
    tempat = models.CharField(max_length=50)
    waktu = models.CharField(max_length=50)
    tanggal = models.CharField(max_length=50)
    file = models.FileField(upload_to='file/', null=True)

    published = models.DateField(auto_now_add=True)
    updated   = models.TimeField(auto_now=True)

    def __str__(self):
        return self.kegiatan


class agenda(models.Model):
    r_kegiatan = models.CharField(max_length=50)
    r_tempat = models.CharField(max_length=50)
    r_waktu = models.CharField(max_length=50)
    r_tanggal = models.CharField(max_length=50)

    published1 = models.DateField(auto_now_add=True)
    updated1   = models.TimeField(auto_now=True)

    def __str__(self):
        return self.r_kegiatan