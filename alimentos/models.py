from django.db import models

class Aliemnto(models.Model):
    nome = models.CharField(max_length=100)
    calorias_100g = models.FloatField()
    proteina_100g = models.FloatField()
    gordura_100g = models.FloatField()
    preçp_kg = models.FloatField()

    def __str__(self):
        return self.nome
    

