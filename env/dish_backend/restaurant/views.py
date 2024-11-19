from django.shortcuts import render

from .models import Restaurant, User
from rest_framework import viewsets
from .serializers import RestaurantSerializer, UserSerializer


class RestaurantViewSet(viewsets.ModelViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_fields = ['city']

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer