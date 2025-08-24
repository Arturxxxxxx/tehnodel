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
            f"Контакт: {lead.contact}\n"
            f"Сообщение: {lead.message or '-'}\n"
            f"Время: {lead.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        # Отправка в Telegram
        url = f"https://api.telegram.org/bot{config('TOKEN')}/sendMessage"
        payload = {
            "chat_id": config('CHAT_ID'),
            "text": text
        }
        r = requests.post(url, json=payload)

        if r.status_code == 200:
            lead.notified = True
            lead.save(update_fields=['notified'])
        else:
            # можно логировать ошибку или планировать ретрай
            pass


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SpecialistUpdateDeleteView(generics.ListCreateAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer