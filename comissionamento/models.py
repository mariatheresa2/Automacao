from django.db import models
from django.contrib.auth.models import User

DISTRIBUIDORA = [
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('MA', 'Maranhão'),
    ('GO', 'Goiás'),
    ('PA', 'Pará'),
    ('PI', 'Piauí'),
    ('RS', 'Rio Grande do Sul'),
]

class Regional(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False,
                            verbose_name='Regional')
    distribuidora = models.CharField(max_length=20, choices=DISTRIBUIDORA, null=False, 
                            blank=False, verbose_name='Distribuidora')
    class Meta():
        verbose_name = "Regional"
        verbose_name_plural = "Regionais"

    def __str__(self):
        return f"{self.distribuidora} - Regional {self.nome}"

class Comissionamento(models.Model):
    distribuidora = models.CharField(max_length=20, choices=DISTRIBUIDORA, null=False, 
                            blank=False, verbose_name='Distribuidora')
    data_solicitacao = models.DateField(auto_now_add=True)
    data_comissionamento = models.DateField(null=False, blank=False)

    class Meta():
        verbose_name = "Comissionamento"
        verbose_name_plural = "Comissionamentos"

    def cadastrar(self):
        self.save()

    def __str__(self):
        return f"Comissionamento {self.pk}"

class ComissionamentoHistorico(models.Model):
    comissionamento = models.ForeignKey(Comissionamento, on_delete=models.CASCADE, related_name='historico')
    campo_alterado = models.CharField(max_length=100)
    valor_anterior = models.CharField(max_length=255)
    valor_novo = models.CharField(max_length=255)
    alterado_em = models.DateTimeField(auto_now_add=True)
    alterado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    CAMPO_NOMES = {
        'distribuidora': 'Distribuidora',
        'data_comissionamento': 'Data do Comissionamento',
    }

    def campo_alterado_friendly(self):
        return self.CAMPO_NOMES.get(self.campo_alterado, self.campo_alterado)