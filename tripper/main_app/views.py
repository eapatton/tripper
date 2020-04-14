from django.shortcuts import render, redirect
from .models import City, Thing, Trip
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# Add the following import

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')  






from . forms import TripForm
##----------------- MELODY AREA ------------------ (line 23)###
@login_required
def trips(request):
	trips = Trip.objects.filter(user=request.user)
	counter = ""
	for i in range(1,trips.count()+1):
		counter = counter + str(i)
	if request.method == 'POST':
		form = TripForm(request.POST)
		if form.is_valid():
			new_Trip = form.save(commit=False)
			new_Trip.user = request.user
			new_Trip.save()

			return redirect('trips')
	else:
		form = TripForm
	context = {'form': form, 'trips': trips, 'counter': counter}
	return render(request, 'trips.html', context)

def trip_details(request, trip_id):
	trip = Trip.objects.get(id=trip_id)
	things = Trip.objects.get(id=trip_id).events.all()
	city = City.objects.filter(trip=trip_id).first
	trip_form = TripForm()
	return render(request, 'trip_details.html', {'trip': trip, 'things': things, 'city': city })


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


def remove_event(request, trip_id, event_id):	
	Trip.objects.get(id=trip_id).events.remove(event_id)

	return redirect('trip_details', trip.id)





##------------------------ MERT AREA -------------------- (LINE 71)##



def city_index(request):
  city = City.objects.all()
  return render(request, 'cities/index.html' , {'cities': city})


def city_detail(request,city_id):
  city = City.objects.get(id=city_id)

  trips = Trip.objects.filter(user=request.user)


  counter = ""
	
  for i in range(1,trips.count()+1):
	  counter = counter + str(i)



  
  return render(request,'cities/detail.html',{"city" : city, "trips" : trips, "counter":counter})


def assoc_thing(request,trip_id,thing_id,city_id):

  Trip.objects.get(id=trip_id).events.add(thing_id)
  return redirect('detail',city_id=city_id)
  
def delete_thing(request,trip_id,thing_id,city_id):

  Trip.objects.get(id=trip_id).events.remove(thing_id)
  return redirect('detail',city_id=city_id)
  


























  ## -------------------------- LIZ AREA ------------------ (LINE 111)##

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('trips')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)