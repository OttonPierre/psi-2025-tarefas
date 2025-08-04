from django.shortcuts import render
from datetime import date
from .models import Tarefa


def index(request):
    tarefa = Tarefa.objects.all()
    contexto = {
        'tarefa': tarefa,
        'hoje': date.today()
    }
    
    
    return render(request, "site/index.html", contexto)
