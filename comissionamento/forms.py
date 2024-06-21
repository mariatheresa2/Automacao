from django import forms
from .models import DriverAt

class DriverAtForm(forms.ModelForm):
    class Meta:
        model = DriverAt
        fields = ('ip', 'porta', 'dnp', 'range_bi', 'range_ai', 'range_bo', 'faixa_ip_se', 'data_de_criacao')