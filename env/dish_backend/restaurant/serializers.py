from .models import Restaurant, ReviewTable

from rest_framework import serializers

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReviewTable
        fields = '__all__'
        
    def validate(self, data):
        # Ensure rating and comment are provided together
        
        if not data.get('review_rating_ovr') or not data.get('review_rating_ovr'):
            raise serializers.ValidationError("Please put in an overall rating")
        if not data.get('review_rating_cat') or not data.get('review_scale_cat'):
            raise serializers.ValidationError("Please put in a dish category rating")
        return data