from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from serializers import DriverSerializer, DriverDetailSerializer, \
    PassengerSerializer, PassengerDetailSerializer
from apps.ubus.models import Driver, Passenger


class DriverList(ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverDetail(RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverDetailSerializer


class PassengerList(ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class PassengerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerDetailSerializer