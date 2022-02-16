from .models import Logo
from rest_framework import serializers


class LogoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Logo
        fields = '__all__'


class LogoListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Logo
        fields = '__all__'
        depth = 1
