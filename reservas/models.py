from django.db import models
from stands.models import Stand


class Reserva(models.Model):
    cnpj = models.CharField(max_length=200)
    nome_empresa = models.CharField(max_length=200)
    categoria_empresa = models.CharField(max_length=200)
    quitado = models.BooleanField(default=False)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
