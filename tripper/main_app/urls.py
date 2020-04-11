from django.urls import path
from . import views

urlpatterns = [

    # Liz
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),







    #Melody
    path('trips/', views.trips, name='trips'),
    path('trips/<int:trip_id>/', views.trip_details, name='tripdetails'),






    # Mert"s Path
    path('cities/', views.city_index, name='destination'),
    path('cities/<int:city_id>/', views.city_detail, name="detail"),
    path('trips/<int:trip_id>/assoc_trip/<int:thing_id>/', views.assoc_thing, name='assoc_thing'),



]