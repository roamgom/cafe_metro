from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('', views.station_root),
    path('station/<int:pk>/', views.StationDetail.as_view(), name='station-detail'),
    path('cafe/<int:pk>/', views.CafeDetail.as_view(), name='cafe-detail'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    # path('user/<int:pk>/', views.UserDetail.as_view(), name='cafeuser-detail'),
]

