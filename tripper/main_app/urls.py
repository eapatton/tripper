from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

















    # Mert"s Path
    path('cities/', views.city_index, name='index'),
]