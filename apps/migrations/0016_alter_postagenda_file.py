# Generated by Django 3.2.7 on 2021-11-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_alter_postagenda_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagenda',
            name='file',
            field=models.FileField(upload_to='file/'),
        ),
    ]
