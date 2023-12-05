from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    date_on_yard = models.DateField()
    style = models.CharField(max_length=100)
    drive_type = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    vin = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    transmission = models.CharField(max_length=101)

 
