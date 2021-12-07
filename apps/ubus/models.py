from django.db import models


class Driver (models.Model):
    point_a = models.CharField(verbose_name='Откуда', max_length=255)
    point_b = models.CharField(verbose_name='Куда', max_length=255)
    date = models.DateField(verbose_name='Когда',)
    car = models.CharField(verbose_name='Машина', max_length=255)
    price = models.IntegerField(verbose_name='Цена')
    phone_number = models.CharField(verbose_name='Номер телефона',
                                    max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return f'Откуда: {self.point_a}, Куда: {self.point_b}'


class Passenger (models.Model):
    point_a = models.CharField(verbose_name='Откуда', max_length=255)
    point_b = models.CharField(verbose_name='Куда', max_length=255)
    date = models.DateField(verbose_name='Когда')
    num_of_passenger = models.CharField(verbose_name='Пассажир', max_length=10)
    phone_number = models.CharField(verbose_name='Номер телефона',
                                    max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пассажир'
        verbose_name_plural = 'Пассажиры'

    def __str__(self):
        return f'Откуда: {self.point_a}, Куда: {self.point_b}'