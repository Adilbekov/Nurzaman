# Generated by Django 5.0 on 2023-12-25 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_choice_alter_blog_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Товары (характеристики)', 'verbose_name_plural': 'Товар (характеристика)'},
        ),
    ]
