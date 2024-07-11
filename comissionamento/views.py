from django.shortcuts import get_object_or_404, render, redirect
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Comissionamento, ComissionamentoHistorico
from .forms import ComissionamentoForm

# Página Inicial
def home(request):
    return render(request, 'comissionamento/home.html')

# Página de testes
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
            instance = form.save(commit=False)
            instance.alterado_por = request.user
            instance.save()
            form.save_m2m()
            return redirect('detalhes_comissionamento', pk=instance.pk)
    else:
        form = ComissionamentoForm(instance=comissionamento)
            
    return render(request, 'comissionamento/formulario_comissionamento.html', {'form': form, 'comissionamento': comissionamento, 'modo': 'edicao'})

def detalhes_comissionamento(request, pk):
    comissionamento = get_object_or_404(Comissionamento, pk=str(pk))
    form = ComissionamentoForm(instance=comissionamento)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    return render(request, 'comissionamento/formulario_comissionamento.html', {'form': form, 'comissionamento': comissionamento, 'modo': 'visualizacao'})

def cancelar_comissionamento(request):
    return render(request, '')

@receiver(pre_save, sender=Comissionamento)
def salvar_historico_comissionamento(sender, instance, **kwargs):

    if instance.pk:
        comissionamento_anterior = Comissionamento.objects.get(pk=instance.pk)
        campos_a_comparar = ['distribuidora', 'data_comissionamento']

        for campo in campos_a_comparar:
            valor_anterior = getattr(comissionamento_anterior, campo)
            valor_novo = getattr(instance, campo)
            if valor_anterior != valor_novo:
                ComissionamentoHistorico.objects.create(
                    comissionamento = instance,
                    campo_alterado = campo,
                    valor_anterior = valor_anterior,
                    valor_novo = valor_novo,
                    alterado_por = instance.alterado_por
                )

def historico_comissionamento(request, pk):
    comissionamento = get_object_or_404(Comissionamento, pk=pk)
    historico = comissionamento.historico.all()
    return render(request, 'comissionamento/historico_comissionamento.html', {'comissionamento': comissionamento, 'historico': historico})