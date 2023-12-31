# Generated by Django 5.0 on 2023-12-24 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_1', models.ImageField(upload_to='setting_logo1', verbose_name='Первый логотип')),
                ('logo_2', models.ImageField(upload_to='logo_setting_2', verbose_name='Второй логотип')),
                ('logo_3', models.ImageField(upload_to='setting_logo3', verbose_name='Третий логотип')),
            ],
            options={
                'verbose_name': 'Логотип',
                'verbose_name_plural': 'Логотипы',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.CharField(max_length=255, verbose_name='Адрес')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('ofice', models.CharField(max_length=255, verbose_name='Офис продаж (локация)')),
                ('work_time', models.CharField(max_length=255, verbose_name='График (время)')),
                ('instagram', models.CharField(max_length=255, verbose_name='Instagram (название)')),
                ('facebook', models.CharField(max_length=255, verbose_name='Fasebook (название)')),
                ('watsap', models.CharField(max_length=255, verbose_name='Wathsap (номер)')),
            ],
            options={
                'verbose_name': 'Основные ностройка',
                'verbose_name_plural': 'Основные ностройки',
            },
        ),
        migrations.CreateModel(
            name='SettingPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефонные номера')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='base.setting')),
            ],
            options={
                'unique_together': {('settings', 'phone')},
            },
        ),
    ]
