from django.db import models

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
