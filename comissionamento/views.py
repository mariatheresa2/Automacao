from django.shortcuts import render
from .models import DriverAt
from django.utils import timezone

def drivers_at(request):
    drivers_at = DriverAt.objects.filter(data_de_criacao__lte=timezone.now()).order_by('data_de_criacao')
    return render(request, 'comissionamento/driver_at.html', {'drivers_at': drivers_at})

def home_page(request):
    return render(request, 'comissionamento/index.html', {})

def visualizar_drivers_at(request):
    drivers_at = DriverAt.objects.filter(data_de_criacao__lte=timezone.now()).order_by('data_de_criacao')
    return render(request, 'comissionamento/visualizar_drivers_at.html', {'drivers_at': drivers_at})