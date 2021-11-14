# Generated by Django 3.2.7 on 2021-11-08 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_alter_postagenda_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegiatan', models.CharField(max_length=50)),
                ('tempat', models.CharField(max_length=50)),
                ('waktu', models.CharField(max_length=50)),
                ('tanggal', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='file/')),
                ('published', models.DateField(auto_now_add=True)),
                ('updated', models.TimeField(auto_now=True)),
            ],
        ),
    ]
