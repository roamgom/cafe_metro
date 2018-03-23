from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework import permissions

from .models import Station, Cafe, Review


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('id', 'line', 'name')


# add queryset like date, star
class CafeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cafe
        fields = ('id', 'station', 'name', 'location', 'score')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'cafe', 'upload_time', 'star', 'review')

