from django.db import models

# Create your models here.

class City(models.Model):
    image = models.CharField(max_length= 500)
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length= 250)

class Thing(models.Model):
    address = models.TextField(max_length= 250)
    description = models.TextField(max_length= 250)
    cost = models.IntegerField()
    hours = models.CharField(max_length= 100)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    
class Trip(models.Model):
    date = models.DateField()
    description = models.TextField(max_length= 250)
    budget = models.IntegerField()
    city = models.ManyToManyField(City)
    things_to_do = models.ManyToManyField(Thing)