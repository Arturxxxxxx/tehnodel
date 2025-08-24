from rest_framework import serializers
from .models import Applications, Product, Specialist


class ApplicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applications
        fields = ['id', 'name', 'phone_number', 'address']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'descriptions']

class SpecialistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialist
        fields = ['id', 'name', 'image', 'speciality', 'experience', 'quantity_reviews', 'rating_reviews']
        