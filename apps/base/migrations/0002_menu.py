# Generated by Django 5.0 on 2023-12-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compani1', models.CharField(max_length=255, verbose_name='О компании')),
                ('compani2', models.CharField(max_length=255, verbose_name='О проекте')),
                ('compani3', models.CharField(max_length=255, verbose_name='Расположение')),
                ('compani4', models.CharField(max_length=255, verbose_name='Преимущества')),
                ('compani5', models.CharField(max_length=255, verbose_name='Выбор')),
                ('compani6', models.CharField(max_length=255, verbose_name='Контакты')),
            ],
        ),
    ]
