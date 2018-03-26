from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework import permissions

from .models import Station, Cafe, Review, CafeUser


class SimpleReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'star')


# add queryset like date, star
class CafeSerializer(serializers.ModelSerializer):
    review_set = SimpleReviewSerializer(many=True)

    class Meta:
        model = Cafe
        fields = ('id', 'station', 'name', 'location', 'get_score', 'review_set')


class SimpleCafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = ('id', 'name', 'score')


class StationSerializer(serializers.ModelSerializer):
    cafe_set = SimpleCafeSerializer(many=True)

    class Meta:
        model = Station
        fields = ('line', 'name', 'cafe_set')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # cafe_set = SimpleCafeSerializer(many=True)

    class Meta:
        model = CafeUser
        fields = '__all__'
