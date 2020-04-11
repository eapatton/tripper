from django.shortcuts import render, redirect
from .models import City, Thing, Trip

# Create your views here.
# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')  










  ##----------------- MELODY AREA ------------------ (line 23)###















































  ##------------------------ MERT AREA -------------------- (LINE 71)##



def city_index(request):
  city = City.objects.all()
  return render(request, 'cities/index.html' , {'cities': city})

def city_detail(request,city_id):
  city = City.objects.get(id=city_id)
  trips = Trip.objects.all()

  
  return render(request,'cities/detail.html',{"city" : city, "trips" : trips})


































  ## -------------------------- LIZ AREA ------------------ (LINE 111)##