from django.db import models

class Alimentos(models.Model):
    nome = models.CharField(max_length=100)
    proteina = models.FloatField()
    carboidrato = models.FloatField()
    gordura = models.FloatField()
    calorias = models.FloatField()
    custo = models.FloatField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

