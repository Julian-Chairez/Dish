from django.shortcuts import render

from .models import Restaurant
from rest_framework import viewsets
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_fields = ['city']
