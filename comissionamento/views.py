from django.shortcuts import get_object_or_404, render, redirect
from .models import Comissionamento
from .forms import ComissionamentoForm

def home(request):
    return render(request, 'comissionamento/home.html')

# Comissionamento
def comissionamentos(request):
    comissionamentos = Comissionamento.objects.all()
    return render(request, 'comissionamento/comissionamentos.html', {'comissionamentos': comissionamentos})

def cadastrar_comissionamento(request):
    if request.method == 'POST':
        form = ComissionamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comissionamentos')
    else:
        form = ComissionamentoForm()
        
    return render(request, 'comissionamento/cadastrar_comissionamento.html', {'form': form})

def editar_comissionamento(request, pk):
    comissionamento = get_object_or_404(Comissionamento, pk=pk)

    if request.method == 'POST':
        form = ComissionamentoForm(request.POST, instance=comissionamento)
        if form.is_valid():
            form.save()
            return redirect('detalhes_comissionamento', comissionamento.pk)
    else:
        form = ComissionamentoForm(instance=comissionamento)
            
    return render(request, 'comissionamento/editar_comissionamento.html', {'form': form, 'comissionamento': comissionamento})

def detalhes_comissionamento(request, pk):
    comissionamentoPk = str(pk)
    comissionamento = get_object_or_404(Comissionamento, pk=comissionamentoPk)
    return render(request, 'comissionamento/detalhes_comissionamento.html', {'comissionamento': comissionamento})

def cancelar_comissionamento(request):
    return render(request, '')
