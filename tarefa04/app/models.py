from django.db import models
from datetime import date

class Tarefa(models.Model):
    Naoconcluida = "Não concluída"
    concluida = "Concluída"
    status_choice = {
        Naoconcluida: "Não concluída",
        concluida: "Concluída",
    }

    nome = models.CharField(max_length=50)
    status = models.CharField(max_length=13, choices=status_choice, default="Não concluída")
    prazo = models.DateField(default='2024-01-01')

    def __str__(self):
        return self.nome
    