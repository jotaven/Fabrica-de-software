from django.shortcuts import redirect, render, get_object_or_404
from .models import List
from .forms import RegistroList

def viewPrincipal(request):
    objects = List.objects.all()
    return render(request, "principal.html", {'objects':objects})

def viewDetalhe(request, id):
    objects = List.objects.all()
    listaProcurar = get_object_or_404(List, pk=id)
    return render(request, "detalhe.html",{"listaPesquisada":listaProcurar, "id":id})

def viewApagar(request, id):
    listaApagada = get_object_or_404(List, pk=id)
    listaApagada.delete()
    return redirect('principal')

def viewCriar(request):
    formulario = RegistroList(request.POST, request.FILES,)
    if formulario.is_valid():
            formulario.save()
            return redirect('principal')

    return render(request, "criar.html", {"formulario":formulario})

def viewAlterar(request, id):
    list_itemAlterado = get_object_or_404(List, pk=id)
    formulario = RegistroList(request.POST or None, instance=list_itemAlterado)

    if formulario.is_valid():
        formulario.save()
        return redirect('principal')

    return render(request, 'alterar.html', {'formulario':formulario})