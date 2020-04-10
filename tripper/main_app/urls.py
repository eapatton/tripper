from django.urls import path
from . import views

urlpatterns = [

    # Liz
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),







    #Melody








    # Mert"s Path
    path('cities/', views.city_index, name='destination'),
    path('cities/<int:city_id>/', views.city_detail, name="detail"),




]