from django.urls import path
from .views import *

urlpatterns = [
    path('drivers/', DriverList.as_view(), name='drivers'),
    path('drivers/<int:pk>/', DriverDetail.as_view()),

    path('passengers/', PassengerList.as_view(), name='passengers'),
    path('passengers/<int:pk>/', PassengerDetail.as_view()),
]