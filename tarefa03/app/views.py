from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def usuarios(request):
    dados_usuario = [
        {"nome": "Pierre", "matricula": "0001", "idade": 17, "cidade": "São Paulo do Potengi"},
        {"nome": "Francisco", "matricula": "0002", "idade": 17, "cidade": "São Paulo do Potengi"},
        {"nome": "Danilo", "matricula": "0003", "idade": 18, "cidade": "Boa Saúde"},
        {"nome": "João", "matricula": "0004", "idade": 17, "cidade": "São Paulo do Potengi"},
        {"nome": "Rafael", "matricula": "0005", "idade": 18, "cidade": "Santa Maria"},
    ]

    context = {
        "usuarios": dados_usuario,
    }
    return render(request, 'usuarios.html', context)