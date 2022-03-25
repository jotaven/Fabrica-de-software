from unicodedata import name
from django.urls import path
from .views import viewAlterar, viewCriar, viewDelete, viewPrincipal, viewDetalhe

urlpatterns = [
    path('principal/', viewPrincipal, name = 'principal'),
    path('postagem/<int:id>/', viewDetalhe, name = 'detalhe'),
    path('deletar/<int:id>/', viewDelete, name = 'delete'),
    path('criar-postagem/', viewCriar, name = 'criar'),
    path('alterar-postagem/<int:id>/', viewAlterar, name = 'alterar'),
]