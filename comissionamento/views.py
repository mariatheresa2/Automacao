from django.shortcuts import get_object_or_404, render, redirect
from .models import DriverAt
from django.utils import timezone
from .forms import DriverAtForm

def drivers_at(request):
    drivers_at = DriverAt.objects.filter(data_de_criacao__lte=timezone.now()).order_by('data_de_criacao')
    return render(request, 'comissionamento/driver_at.html', {'drivers_at': drivers_at})

def home_page(request):
    return render(request, 'comissionamento/index.html', {})

def visualizar_drivers_at(request):
    drivers_at = DriverAt.objects.filter(data_de_criacao__lte=timezone.now()).order_by('data_de_criacao')
    return render(request, 'comissionamento/visualizar_drivers_at.html', {'drivers_at': drivers_at})

def criar_driver_at(request):
    if request.method == "POST":
        form = DriverAtForm(request.POST)
        if form.is_valid():
            driver_at = form.save(commit=False)
            driver_at.ip = request.user
            '''driver_at.porta = request.user
            driver_at.dnp = request.user
            driver_at.range_bi = request.user
            driver_at.range_ai = request.user
            driver_at.range_bo = request.user
            driver_at.faixa_ip_se = request.user'''
            driver_at.data_de_criacao = timezone.now()
            driver_at.save()
            return redirect('detalhes_drivers_at', pk=driver_at.pk)
    else:  
        form = DriverAtForm()

    return render(request, 'comissionamento/editar_driver_at.html', {'form': form})

def driver_at_editar(request, pk):
     post = get_object_or_404(DriverAt, pk=pk)
     if request.method == "POST":
         form = DriverAtForm(request.POST, instance=post)
         if form.is_valid():
             driver_at = form.save(commit=False)
             driver_at.ip = request.user
             driver_at.data_de_criacao = timezone.now()
             driver_at.save()
             return redirect('driver_at_detalhes', pk=driver_at.pk)
     else:
         form = DriverAtForm(instance=driver_at)
     return render(request, 'blog/driver_at_editar.html', {'form': form})

def detalhes_drivers_at(request, pk):
    driver_at = get_object_or_404(DriverAt, pk=pk)
    return render(request, 'blog/post_detail.html', {'driver_at': driver_at})