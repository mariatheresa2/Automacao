from django.urls import path
from . import views

urlpatterns = [
    path('driversAT', views.drivers_at, name='drivers_at'),
    path('', views.home_page, name='home_page'),
    path('driversAT/visualizar', views.visualizar_drivers_at, name='visualizar_drivers_at')
]