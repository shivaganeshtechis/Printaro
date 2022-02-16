from .models import Tshirt
from rest_framework import serializers


class TshirtSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Tshirt
        fields = '__all__'


class TshirtListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Tshirt
        fields = '__all__'
        depth = 1
