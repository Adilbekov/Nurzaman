# Generated by Django 5.0 on 2023-12-24 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name': 'Слайд', 'verbose_name_plural': 'Слайды'},
        ),
    ]
