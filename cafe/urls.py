from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    # path('', views.),
    path('station/<int:station_pk>/', views.StationDetail.as_view(), name='station-detail'),
    path('station/<int:station_pk>/cafe/', views.CafeList.as_view(), name='cafe-list'),
    path('station/<int:station_pk>/cafe/<int:cafe_pk>/', views.CafeDetail.as_view(), name='cafe-detail'),
    path('station/<int:station_pk>/cafe/<int:cafe_pk>/review/', views.ReviewList.as_view(), name='review-list'),
    path('station/<int:station_pk>/cafe/<int:cafe_pk>/review/<int:review_pk>', views.ReviewDetail.as_view(), name='review-detail'),
]

