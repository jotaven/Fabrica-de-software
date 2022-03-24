from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import RegistroPost

def viewPrincipal(request):

    posts = Post.objects.all()
    return render(request, 'principal.html', {'posts':posts})

def viewDetalhe(request, id):

    posts = Post.objects.all()

    postagemProcurada = get_object_or_404(Post, pk=id)

    return render(request, 'detalhe.html', {'postagemPesquisada':postagemProcurada, 'id':id})

def viewDelete(request, id):
    postagemDeletada = get_object_or_404(Post, pk=id)

    postagemDeletada.delete()

    return redirect('principal')

def viewCriar(request):
    formulario = RegistroPost(request.POST, request.FILES,)

    if formulario.is_valid():
        formulario.save()
        return redirect('principal')

    return render(request, 'criar.html', {'formulario':formulario})

def viewAlterar(request, id):
    postagemAlterada = get_object_or_404(Post, pk=id)
    formulario = RegistroPost(request.POST or None, instance=postagemAlterada)

    if formulario.is_valid():
        formulario.save()
        return redirect('principal')

    return render(request, 'alterar.html', {'formulario':formulario})