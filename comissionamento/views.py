from django.shortcuts import get_object_or_404, render, redirect
from .models import Comissionamento
from .forms import ComissionamentoForm

def home(request):
    return render(request, 'comissionamento/home.html')

def teste(request):
    comissionamentos = Comissionamento.objects.all()
    return render(request, 'comissionamento/teste.html', {'comissionamentos': comissionamentos})

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
        
    return render(request, 'comissionamento/formulario_comissionamento.html', {'form': form, 'modo': 'cadastro'})

def editar_comissionamento(request, pk):
    comissionamento = get_object_or_404(Comissionamento, pk=pk)

    if request.method == 'POST':
        form = ComissionamentoForm(request.POST, instance=comissionamento)
        if form.is_valid():
            form.save()
            return redirect('detalhes_comissionamento', comissionamento.pk)
    else:
        form = ComissionamentoForm(instance=comissionamento)
        print(comissionamento.data_comissionamento)
            
    return render(request, 'comissionamento/formulario_comissionamento.html', {'form': form, 'comissionamento': comissionamento, 'modo': 'edicao'})

def detalhes_comissionamento(request, pk):
    comissionamento = get_object_or_404(Comissionamento, pk=str(pk))
    form = ComissionamentoForm(instance=comissionamento)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    return render(request, 'comissionamento/formulario_comissionamento.html', {'form': form, 'comissionamento': comissionamento, 'modo': 'visualizacao'})

def cancelar_comissionamento(request):
    return render(request, '')
