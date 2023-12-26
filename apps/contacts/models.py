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