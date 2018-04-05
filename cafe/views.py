from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser

from .models import Station, Cafe, Review, CafeUser
from .serializers import StationSerializer
from .serializers import CafeSerializer
from .serializers import ReviewSerializer
from .serializers import UserSerializer
from .serializers import StationListSerializer


class StationList(generics.ListAPIView):

    queryset = Station.objects.all()
    serializer_class = StationListSerializer


class StationDetail(generics.RetrieveUpdateDestroyAPIView):

    # permission_classes = IsAdminUser

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class CafeDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = IsAuthenticatedOrReadOnly

    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = IsAuthenticatedOrReadOnly
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (SessionAuthentication, BaseAuthentication)
    # permission_classes = IsAuthenticated

    queryset = CafeUser.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def station_root(request, format=None):
    return Response('cafe-metro api v1')
