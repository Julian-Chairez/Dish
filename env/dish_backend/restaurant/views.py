from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from .models import Restaurant, ReviewTable
from rest_framework import viewsets
from .serializers import RestaurantSerializer,ReviewSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_fields = ['city','state']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewTable.objects.all()
    serializer_class = ReviewSerializer
    def review_list(request):
        if request.method == 'POST':
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
