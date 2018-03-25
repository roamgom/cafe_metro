from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework import permissions

from .models import Station, Cafe, Review


class SimpleReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('url', 'id', 'title', 'star')


# add queryset like date, star
class CafeSerializer(serializers.HyperlinkedModelSerializer):
    review_set = SimpleReviewSerializer(many=True)

    class Meta:
        model = Cafe
        fields = ('url', 'id', 'station', 'name', 'location', 'get_score', 'review_set')


class SimpleCafeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cafe
        fields = ('url', 'id', 'name', 'score')


class StationSerializer(serializers.HyperlinkedModelSerializer):
    cafe_set = SimpleCafeSerializer(many=True)

    class Meta:
        model = Station
        fields = ('url', 'line', 'name', 'cafe_set')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
