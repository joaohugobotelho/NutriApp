from django.db import models


class Usuario(models.Model):

    OBJETIVOS_CHOICES = [
        ('emagrecer', 'Emagrecer'),
        ('manter', 'Manter peso'),
        ('massa', 'Ganhar massa'),
    ]

    DEFICIT_CHOICES = [
        ('manutencao', "Manutenção"),
        ('leve', 'Déficit leve'),
        ('moderado', 'Déficit Moderado'),
        ('agressivo', 'Déficit agressivo'),
    ]

    ATIVIDADE_CHOICES = [
        ('sedentario', 'Sedentário'),
        ('leve', 'Leve'),
        ('moderado', 'Moderado'),
        ('intenso', 'Intenso'),
    ]


    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    objetivo = models.CharField(max_length=20, choices=OBJETIVOS_CHOICES)
    tipo_deficit = models.CharField(max_length=20, choices=DEFICIT_CHOICES)
    atividade = models.CharField(max_length=20, choices=ATIVIDADE_CHOICES)


    def __str__(self):
        return self.nome
