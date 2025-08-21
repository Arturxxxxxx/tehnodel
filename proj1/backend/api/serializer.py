from rest_framework import serializers
from .models import Applications, Product


class ApplicationsSerializer(serializers.ModelSerializer):

    class Meta:
        models = Applications
        feilds = ['id', 'name', 'phone_number', 'address']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        models = Product
        feilds = ['id', 'name', 'image', 'descriptions']