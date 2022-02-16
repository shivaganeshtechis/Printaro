from apps.tshirts.serializers import TshirtListSerializer
from apps.logos.serializers import LogoListSerializer
from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    student = TshirtListSerializer()
    application = LogoListSerializer()

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
