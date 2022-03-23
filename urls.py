from django.urls import path
from .views import viewPrincipal
from .views import viewSecundaria

urlpatterns = [
    path('principal/', viewPrincipal, name = 'principal'),
    path('secundaria/', viewSecundaria, name = 'secundaria')
]