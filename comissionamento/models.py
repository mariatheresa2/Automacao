from django.conf import settings
from django.db import models
from django.utils import timezone

class DriverAt(models.Model):
    ip = models.CharField(max_length=20)
    porta = models.IntegerField()
    dnp = models.IntegerField()
    range_bi = models.CharField(max_length=10)
    range_ai = models.CharField(max_length=10)
    range_bo = models.CharField(max_length=10)
    faixa_ip_se = models.CharField(max_length=20)
    data_de_criacao = models.DateTimeField(blank=True, null=True)

    def criar_driver_at(self):
        self.data_de_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.ip