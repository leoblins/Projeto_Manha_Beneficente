from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('contatos/', views.contatos, name='contatos'),
    path('acoes/', views.acoes_realizadas, name='acoes'),  # <- aqui está o nome da rota
    path('transparencia/', views.transparencia, name='transparencia'),
]
