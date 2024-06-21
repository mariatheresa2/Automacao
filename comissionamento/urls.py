from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('driversAT/', views.drivers_at, name='drivers_at'),
    path('driversAT/criar/', views.criar_driver_at, name='criar_driver_at'),
    path('driversAT/visualizar/', views.visualizar_drivers_at, name='visualizar_drivers_at'),
    path('driversAT/{int:pk}/', views.detalhes_drivers_at, name='detalhes_drivers_at'),
    path('driver_at/<int:pk>/editar/', views.driver_at_editar, name='driver_at_editar'),
]