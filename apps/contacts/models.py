from django.db import models

# Create your models here.

class Cotact(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    email=models.EmailField(
        verbose_name='Электронная почта'
    )
    phone=models.CharField(
        max_length=255,
        verbose_name='Телефонный номер'
    )
    
    def __str__(self):
        return f'{self.name} - {self.phone}'
    
    class Meta:
        verbose_name='Запросы для обратной связи'
        verbose_name_plural='Запрос для обратной связи'


class Contact_2(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    phone=models.CharField(
        max_length=255,
        verbose_name='Телефонный номер'
    )
    
    def __str__(self):
        return f'{self.name} - {self.phone}'
    
    class Meta:
        verbose_name='Заказать звонки'
        verbose_name_plural='Заказать звонк'


class Contact_3(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    phone=models.CharField(
        max_length=255,
        verbose_name='Телефонный номер'
    )
    
    def __str__(self):
        return f'{self.name} - {self.phone}'
    
    class Meta:
        verbose_name='Дополнительные данные для обработки'
        verbose_name_plural='Дополнительные данные'