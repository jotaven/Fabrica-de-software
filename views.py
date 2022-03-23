from django.shortcuts import render

def viewPrincipal(request):
    return render(request, 'principal.html')

def viewSecundaria(request):
    return render(request, 'secundaria.html')
