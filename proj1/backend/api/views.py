from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Applications, Product, Specialist
from .serializer import ApplicationsSerializer, ProductSerializer, SpecialistSerializer
import requests
from decouple import config




class ApplicationsViews(generics.CreateAPIView):
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

    def perform_create(self, serializer):
        lead = serializer.save()

        # Формируем текст для Телеграма
        text = (
            f"🆕 Новая заявка\n"
            f"Имя: {lead.name}\n"
            f"Контакт: {lead.phone_number}\n"
            f'Адрес: {lead.address}'
        )

        # Отправка в Telegram
        url = f"https://api.telegram.org/bot{config('TOKEN')}/sendMessage"
        payload = {
            "chat_id": config('CHAT_ID'),
            "text": text
        }
        r = requests.post(url, json=payload)


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SpecialistUpdateDeleteView(generics.ListCreateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer