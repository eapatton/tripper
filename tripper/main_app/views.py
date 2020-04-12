from django.shortcuts import render, redirect
from .models import City, Thing, Trip
# Create your views here.
# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')  










from . forms import TripForm
##----------------- MELODY AREA ------------------ (line 23)###
def trips(request):
	trips = Trip.objects.all()

	if request.method == 'POST':
		form = TripForm(request.POST)
		if form.is_valid():
			new_Trip = form.save()
			return redirect('trips')
	else:
		form = TripForm
	context = {'form': form, 'trips': trips}
	return render(request, 'trips.html', context)

def trip_details(request, trip_id):
	trip = Trip.objects.get(id=trip_id)
	things = Trip.objects.get(id=trip_id).events.all()
	trip_form = TripForm()
	# city = Trip.objects. 'city':city
	return render(request, 'trip_details.html', {'trip': trip, 'things': things })

def trip_delete(request, trip_id):
	Trip.objects.get(id=trip_id).delete()
	return redirect('trips')

def trip_update(request, trip_id):
	trip = Trip.objects.get(id=trip_id)

	if request.method == 'POST':
		form = TripForm(request.POST, instance=trip)
		if form.is_valid():
			new_Trip = form.save()
			return redirect('trip_details', trip.id)
	else:
		form = TripForm(instance=trip)
	return render(request, 'trip_update.html', {'form': form})
























##------------------------ MERT AREA -------------------- (LINE 71)##



def city_index(request):
  city = City.objects.all()
  return render(request, 'cities/index.html' , {'cities': city})

def city_detail(request,city_id):
  city = City.objects.get(id=city_id)
  trips = Trip.objects.all()

  
  return render(request,'cities/detail.html',{"city" : city, "trips" : trips})

def assoc_thing(request,trip_id,thing_id,city_id):

  Trip.objects.get(id=trip_id).events.add(thing_id)
  return redirect('detail',city_id=city_id)
  

























  ## -------------------------- LIZ AREA ------------------ (LINE 111)##