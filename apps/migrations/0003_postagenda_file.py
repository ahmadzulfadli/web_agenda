# Generated by Django 3.2.7 on 2021-11-01 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20211101_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagenda',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
