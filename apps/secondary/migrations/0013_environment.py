# Generated by Django 5.0 on 2023-12-25 18:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0012_slidetwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Environment_image', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название обекта')),
                ('descriptions_1', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('descriptions_2', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('descriptions_3', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('descriptions_4', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('descriptions_5', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('descriptions_6', ckeditor.fields.RichTextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Окружение обекта',
                'verbose_name_plural': 'Окружение обекта',
            },
        ),
    ]
