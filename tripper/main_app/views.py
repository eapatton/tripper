<<<<<<< HEAD
from django.shortcuts import render
from .models import City, Thing, Trip
=======
from django.shortcuts import render, redirect
from .models import City, Thing, Trip

>>>>>>> submaster
# Create your views here.
# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')  





##----------------- MELODY AREA ------------------ (line 23)###
def trips(request):
	trips = Trip.objects.all()
	return render(request, 'trips.html' , {'trips': trips} )

def trip_details(request, trip_id):
	trip = Trip.objects.get(id=trip_id)
	#ttd = Trip.objects.things_to_do.all()
	return render(request, 'trip_details.html', {'trip': trip})







































##------------------------ MERT AREA -------------------- (LINE 71)##



def city_index(request):
  city = City.objects.all()
  return render(request, 'cities/index.html' , {'cities': city})

def city_detail(request,city_id):
  city = City.objects.get(id=city_id)
  trip = Trip.objects.first().city.get(id=city_id).thing_set.all()
  return render(request,'cities/detail.html',{"city" : city, "trips" :trip,})


































  ## -------------------------- LIZ AREA ------------------ (LINE 111)##