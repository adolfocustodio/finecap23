from django.db import models


class Stand(models.Model):
    localizacao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.localizacao
