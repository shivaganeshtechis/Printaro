
from rest_framework import generics
from apps.users.mixins import CustomLoginRequiredMixin
from .models import User
from .serializers import UserSerializer, UserSignInSerializer, UserSignUpSerializer


class UserList(CustomLoginRequiredMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer


class UserSignIn(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer
