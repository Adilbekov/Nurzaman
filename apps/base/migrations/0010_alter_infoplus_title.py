# Generated by Django 5.0 on 2023-12-25 14:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_infoplus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoplus',
            name='title',
            field=ckeditor.fields.RichTextField(verbose_name='Название'),
        ),
    ]
