from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    image = models.URLField(default="https://globalcenters.columbia.edu/sites/default/files/styles/cu_crop/public/content/istanbul/visiting%20city/istanbul%20002.jpg?h=eba642ff&itok=rOu6u0xq  `")
    name = models.CharField(max_length= 100)
    description = models.TextField(max_length= 250)
   
    def __str__(self):
        return self.name
    
class Thing(models.Model):
    address = models.TextField(max_length= 250)
    description = models.TextField(max_length= 250)
    cost = models.IntegerField()
    image = models.URLField(default="https://globalcenters.columbia.edu/sites/default/files/styles/cu_crop/public/content/istanbul/visiting%20city/istanbul%20002.jpg?h=eba642ff&itok=rOu6u0xq")
    hours = models.CharField(max_length= 100)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    
    
class Trip(models.Model):
    date = models.DateField()
    description = models.TextField(max_length= 250)
    budget = models.IntegerField()
    city = models.ManyToManyField(City)
    events = models.ManyToManyField(Thing)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
