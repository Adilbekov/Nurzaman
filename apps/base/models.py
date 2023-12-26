from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Logo(models.Model):
    logo_1=models.ImageField(
        upload_to='setting_logo1',
        verbose_name='Первый логотип'
    )
    logo_2=models.ImageField(
        upload_to='logo_setting_2',
        verbose_name='Второй логотип'
    )
    logo_3=models.ImageField(
        upload_to='setting_logo3',
        verbose_name='Третий логотип'
    )

    class Meta:
        verbose_name='Логотип'
        verbose_name_plural='Логотипы'




class Setting(models.Model):
    adres=models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    email=models.EmailField(
        max_length=255,
        verbose_name='Email'
    )
    ofice=models.CharField(
        max_length=255,
        verbose_name='Офис продаж (локация)'
    )
    work_time=models.CharField(
        max_length=255,
        verbose_name='График (время)'
    )
    instagram=models.CharField(
        max_length=255,
        verbose_name='Instagram (название)'
    )
    facebook=models.CharField(
        max_length=255,
        verbose_name='Fasebook (название)'
    )
    watsap=models.CharField(
        max_length=255,
        verbose_name='Wathsap (номер)'
    )
    def __str__(self):
        return self.adres
    
    class Meta:
        verbose_name='Основные ностройка'
        verbose_name_plural='Основные ностройки'

class SettingPhone(models.Model):
    settings=models.ForeignKey(Setting, related_name='options', on_delete=models.CASCADE)
    phone=models.CharField(
        verbose_name='Телефонные номера',
        max_length=255
    )

    class Meta:
        unique_together=('settings', 'phone')

class Menu(models.Model):
    compani1=models.CharField(
        max_length=255,
        verbose_name='О компании'
    )
    compani2=models.CharField(
        max_length=255,
        verbose_name='О проекте'
    )
    compani3=models.CharField(
        max_length=255,
        verbose_name='Расположение'
    )
    compani4=models.CharField(
        max_length=255,
        verbose_name='Преимущества'
    )
    compani5=models.CharField(
        max_length=255,
        verbose_name='Выбор'
    )
    ompani6=models.CharField(
        max_length=255,
        verbose_name='Контакты'
    )

    def __str__(self):
        return self.compani1
    
    class Meta:
        verbose_name='Менюшка'
        verbose_name_plural='Меню'

class About(models.Model):
    image=models.ImageField(
        upload_to='about_image',
        verbose_name='Главная фотография'
    )
    image_2=models.ImageField(
        upload_to='about_image_2',
        verbose_name='Фотография'
    )
    descriptions=RichTextField(
        verbose_name='Описание',
        blank=True, null=True
    )

    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name='О нас'
        verbose_name_plural='О нас'


class Blog(models.Model):
    descriptions_1=RichTextField(
        verbose_name='Информация и достижение',
        blank=True, null=True
    )
    descriptions_2=RichTextField(
        verbose_name='Информация и достижение',
        blank=True, null=True
    )
    descriptions_3=RichTextField(
        verbose_name='Информация и достижение',
        blank=True, null=True
    )
    descriptions_4=RichTextField(
        verbose_name='Информация и достижение',
        blank=True, null=True
    )
    descriptions_5=RichTextField(
        verbose_name='Информация и достижение',
        blank=True, null=True
    )
    descriptions_6=RichTextField(
        verbose_name='Информация и достижение',
        blank=True, null=True
    )

    def __str__(self):
        return self.descriptions_1
    
    class Meta:
        verbose_name='Нам есть чем гордиться (blog)'
        verbose_name_plural='Нам есть чем гордиться (blogs)'
    

class InfoPlus(models.Model):
    image=models.ImageField(
        upload_to='infoPlus_image',
        verbose_name='Фотография'
    )
    title=RichTextField(
        verbose_name='Название'
    )
    descriptions_1=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_2=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_3=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_4=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_5=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_6=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_7=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_8=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_9=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_10=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    descriptions_11=RichTextField(
        verbose_name='приемущесво',
        blank=True, null=True
    )
    def __str__(self):
        return self.descriptions_1
    
    class Meta:
        verbose_name='Приемущесво'
        verbose_name_plural='Приемущесво'


class Choice(models.Model):
    image=models.ImageField(
        upload_to='Choice_image',
        verbose_name='Фотография'
    )
    titlle=models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    title1=models.CharField(
        max_length=255,
        verbose_name='Информация'
    )
    description1=models.CharField(
 
 max_length=255,       verbose_name='Характериска'
    )
    title2=models.CharField(
        max_length=255,
        verbose_name='Информация'
    )
    description2=models.CharField(
 
 max_length=255,       verbose_name='Характериска'
    )
    title3=models.CharField(
        max_length=255,
        verbose_name='Информация'
    )
    description3=models.CharField(
 
 max_length=255,       verbose_name='Характериска'
    )
    title4=models.CharField(
        max_length=255,
        verbose_name='Информация'
    )
    description4=models.CharField(
 
 max_length=255,       verbose_name='Характериска'
    )
    title5=models.CharField(
        max_length=255,
        verbose_name='Информация'
    )
    description5=models.CharField(
 
 max_length=255,       verbose_name='Характериска'
    )
    title6=models.CharField(
        max_length=255,
        verbose_name='Информация'
    )
    description6=models.CharField(
 
 max_length=255,       verbose_name='Характериска'
    )

    def __str__(self):
        return f'{self.titlle} - {self.description1}'
    
    class Meta:
        verbose_name='Товары (характеристики)'
        verbose_name_plural='Товар (характеристика)'