from unicodedata import name
from django.urls import path
from .views import viewApagar, viewCriar, viewDetalhe, viewPrincipal

urlpatterns = [
       path("principal/", viewPrincipal, name = "principal"),
       path('list-item/<int:id>/', viewDetalhe, name='detalhe'),
       path('apagar/<int:id>/', viewApagar, name='apague'),
       path('criar-item', viewCriar, name='criar')
]