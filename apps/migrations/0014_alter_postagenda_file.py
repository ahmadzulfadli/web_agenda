# Generated by Django 3.2.7 on 2021-11-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_auto_20211108_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagenda',
            name='file',
            field=models.FileField(null=True, upload_to='file/'),
        ),
    ]
