from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')













  ##----------------- MELODY AREA ------------------ (line 23)###















































  ##------------------------ MERT AREA -------------------- (LINE 71)##



def city_index(request):
  city = City.objects.all()
  return render(request, 'cities/index.html' , {'cities': city})




































  ## -------------------------- LIZ AREA ------------------ (LINE 111)##