
from rest_framework import generics
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Station, Cafe, Review
from .serializers import StationSerializer
from .serializers import CafeSerializer
from .serializers import ReviewSerializer


class StationDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class CafeList(generics.ListCreateAPIView):

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


class CafeDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


class ReviewList(generics.ListCreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@api_view(['GET'])
def station_root(request, format=None):
    return Response({
        'station': request('station-detail', request=request, format=format),
        'cafe': reverse('cafe-list', request=request, format=format),
    })

