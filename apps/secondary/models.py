from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Slide(models.Model):
    image=models.ImageField(
        upload_to='slide_image',
        verbose_name='Фотография'
    )
    title=models.CharField(
        max_length =255,
        verbose_name='Название'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Слайд'
        verbose_name_plural='Слайды'

class Partners(models.Model):
    image=models.ImageField(
        upload_to='projects_image',
        verbose_name='Логотип партнера'
    )
    
    class Meta:
        verbose_name='Партнер'
        verbose_name_plural='Партнеры'

class Info(models.Model):
    image=models.ImageField(
        verbose_name='Фотография',
        upload_to='info_image'
    )
    title=models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    descriptions=RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Слайд (информация об обекте)'
        verbose_name_plural='Слайды и информация об обекте'

class ImageGallery(models.Model):
    title=models.CharField(
        verbose_name='Название',
        max_length=255
    )
    descriptions=RichTextField(
        verbose_name='Описание'
    )
    image1=models.ImageField(
        upload_to='ImageGellery_image2',
        verbose_name='Первая фотография'
    )
    image2=models.ImageField(
        upload_to='ImageGellery_image1',
        verbose_name='Вторая фотография'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Галерея с фотографиями'
        verbose_name_plural='Галерея с фотографиями'

class One(models.Model):
    title=models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    descrioptions=RichTextField(
        verbose_name='Описание'
    )
    image1=models.ImageField(
        upload_to='Number1_image',
        verbose_name='Фоновая фотография'
    )
    image2=models.ImageField(
        upload_to='Number_image2',
        verbose_name='Основная фотография'
    )
    name=models.CharField(
        max_length=255,
        verbose_name='Приемущество'
    )
    descrioption=RichTextField(
        verbose_name='Описание о приемуществе'
    )

    def __str__(self):
        return f'{self.title} - {self.descrioptions}'
    
    class Meta:
        verbose_name='Приемущество - 1'
        verbose_name_plural='Приемущество - 1'

class SlideTwo(models.Model):
    image=models.ImageField(
        upload_to='SlideTwo_image',
        verbose_name='Фотография'
    )
    title=models.CharField(
        verbose_name='Название',
        max_length=255
    )
    descriptions=RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return f'{self.title} - {self.descriptions}'
    
    class Meta:
        verbose_name='Приемущество - 2'
        verbose_name_plural='Приемущество - 2'

class Environment(models.Model):
    image=models.ImageField(
        upload_to='Environment_image',
        verbose_name='Фотография'
    )
    title=models.CharField(
        max_length=255,
        verbose_name='Название обекта'
    )
    descriptions_1=RichTextField(
        verbose_name='Описание'
    )
    descriptions_2=RichTextField(
        verbose_name='Описание'
    )
    descriptions_3=RichTextField(
        verbose_name='Описание'
    )
    descriptions_4=RichTextField(
        verbose_name='Описание'
    )
    descriptions_5=RichTextField(
        verbose_name='Описание'
    )
    descriptions_6=RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return f'{self.title} - {self.descriptions_1}'
    
    class Meta:
        verbose_name='Окружение обекта'
        verbose_name_plural='Окружение обекта'

class Street(models.Model):
    name=RichTextField(
        verbose_name = 'Название улицы'
    )
    description=RichTextField(
        verbose_name='Описание'
    )

    def _str__(self):
        return f'{self.name} - {self.description}'
    
    class Meta:
        verbose_name='Улица'
        verbose_name_plural='Улица'