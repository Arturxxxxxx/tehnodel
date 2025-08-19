from django.db import models


class Applications(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя Фамилия')
    phone_number = models.IntegerField(max_length=25, verbose_name='Телефон номер')
    address = models.CharField(max_length=50, verbose_name='Адрес клиента')

    def __str__(self):
        return f'{self.name} ({self.phone_number})'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название техники')
    image = models.ImageField(blank=True, null=True, upload_to='/product', verbose_name='фотография')
    descriptions = models.CharField(blank=True, null=True, verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)