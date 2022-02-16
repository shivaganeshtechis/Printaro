from rest_framework import generics
from .serializers import LogoSerializer, LogoListSerializer
from .models import Logo


class LogoList(generics.ListAPIView):
    # Get all posts, limit = 20
    queryset = Logo.objects.all()
    serializer_class = LogoListSerializer


class LogoAdd(generics.CreateAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


class LogoUpdate(generics.UpdateAPIView):
    serializer_class = LogoSerializer
    queryset = Logo.objects.all()
    lookup_field = 'id'


class LogoDelete(generics.DestroyAPIView):
    serializer_class = LogoSerializer
    queryset = Logo.objects.all()
    lookup_field = 'id'
