from rest_framework import serializers
from apps.ubus.models import Driver, Passenger


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ('id', 'point_a', 'point_b', 'date', 'car', 'price',
                  'phone_number',
                  )


class DriverDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = ('id', 'point_a', 'point_b', 'date', 'car', 'price',
                  'phone_number',
                  )


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = ('id', 'point_a', 'point_b', 'date', 'num_of_passenger',
                  'phone_number',
                  )


class PassengerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = ('id', 'point_a', 'point_b', 'date', 'num_of_passenger',
                  'phone_number',
                  )