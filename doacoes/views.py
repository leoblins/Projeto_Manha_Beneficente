from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import RegistroDoacoes

def transparencia(request):
    registro = RegistroDoacoes.objects.last()
    return render(request, 'transparencia.html', {'registro': registro})

def index(request):
    return render(request, 'index.html')

def acoes_realizadas(request):
    return render(request, 'Acoes_Realizadas.html')

def contatos(request):
    return render(request, 'contatos.html')

def quemsomos(request):
    return render(request, 'quemsomos.html')