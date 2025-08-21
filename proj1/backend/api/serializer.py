from rest_framework import serializers
from .models import Applications, Product


class ApplicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applications
        fields = ['id', 'name', 'phone_number', 'address']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'descriptions']