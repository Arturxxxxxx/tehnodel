from django.db import models


class Applications(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя Фамилия')
    phone_number = models.CharField(max_length=25, verbose_name='Телефон номер')
    address = models.CharField(max_length=50, verbose_name='Адрес клиента')

    def __str__(self):
        return f'{self.name} ({self.phone_number})'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название техники')
    image = models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='фотография')
    descriptions = models.CharField(blank=True, null=True, verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Specialist(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    image = models.ImageField(blank=True, null=True, upload_to='specialist/', verbose_name='фотография')
    speciality = models.CharField(max_length=50, blank=True, null=True, verbose_name='специальность')
    experience = models.CharField(max_length=100, blank=True, null=True, verbose_name='опыт работы')
    quantity_reviews = models.CharField(max_length=20, blank=True, null=True, verbose_name='количество отзывов')
    rating_reviews = models.CharField(max_length=20, blank=True, null=True, verbose_name='рейтинг отзывов')