from rest_framework import generics
from .serializers import ProductSerializer, ProductListSerializer
from .models import Product
from config.constants import *


class Productist(generics.ListAPIView):
    # Get all posts, limit = 20
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductAdd(generics.CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'


class ProductUpdate(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'


class ProductDelete(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
