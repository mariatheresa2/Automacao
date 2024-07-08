from django.forms import ModelForm, DateField, DateInput
from .models import Comissionamento

class ComissionamentoForm(ModelForm):
    data_comissionamento = DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label='Data de Comissionamento'
    )
    class Meta:
        model = Comissionamento
        fields = ['distribuidora', 'data_comissionamento']
