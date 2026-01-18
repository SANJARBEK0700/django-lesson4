from django.db import models

# Create your models here.
class Avtosalon(models.Model):
    car_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    brand = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self.car_name
