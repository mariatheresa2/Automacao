from django.forms import ModelForm, DateField, DateInput, TextInput, CharField
from .models import Comissionamento

class ComissionamentoForm(ModelForm):
    data_comissionamento = DateField(
        label='Data de Comissionamento',
        widget=DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
    )
    class Meta:
        model = Comissionamento
        fields = ['distribuidora', 'data_comissionamento']
