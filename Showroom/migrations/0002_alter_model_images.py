# Generated by Django 4.2.3 on 2023-08-21 09:49

import django.core.files.storage
from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ("Showroom", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="model",
            name="images",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(
                    location=pathlib.PureWindowsPath(
                        "D:/code files/aws_mzr/Django/(6) Showroom and blog website together/media"
                    )
                ),
                upload_to="",
            ),
        ),
    ]