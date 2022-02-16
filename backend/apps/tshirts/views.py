from rest_framework import generics
from .serializers import TshirtSerializer, TshirtListSerializer
from .models import Tshirt
import random
from config.constants import *


class Tshirtist(generics.ListAPIView):
    # Get all posts, limit = 20
    queryset = Tshirt.objects.all()
    serializer_class = TshirtListSerializer


class TshirtAdd(generics.CreateAPIView):
    queryset = Tshirt.objects.all()
    serializer_class = TshirtSerializer

    def post(self, request, *args, **kwargs):

        serializer = TshirtSerializer()
        serializer.validate(request.data)

        color_code = "#{:06x}".format(random.radint(0, 0xFFFFFFF))

        request.data._mutable = True
        request.data['color_code'] = request.data['color_code'] if 'color_code' in request.data else color_code

        return self.create(request, *args, **kwargs)


class TshirtUpdate(generics.UpdateAPIView):
    serializer_class = TshirtSerializer
    queryset = Tshirt.objects.all()
    lookup_field = 'id'


class TshirtDelete(generics.DestroyAPIView):
    serializer_class = TshirtSerializer
    queryset = Tshirt.objects.all()
    lookup_field = 'id'
