from django.contrib import admin

from apps.ubus.models import Driver, Passenger


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['point_a', 'point_b', 'date', 'car', 'price',
                    'phone_number', 'create_at']


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['point_a', 'point_b', 'date', 'passengers',
                    'phone_number', 'create_at']