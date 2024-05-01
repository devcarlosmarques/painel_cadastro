from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms


def cadastro_produto(request):
    if request.method == "POST":

        nome_produto = request.POST.get('campo_nome')

        if Produtos.objects.filter(nome=nome_produto):
            messages.error(request,f'O produto {nome_produto} já está cadastrado.')

        else:
            bd = Produtos()
            bd.nome = request.POST.get('campo_nome')
            bd.quantidade = request.POST.get('campo_quantidade')
            bd.preco = request.POST.get('campo_preco')
            bd.save()
            messages.success(request,f'O produto {nome_produto} foi cadastrado.')

    return render(request,'cadastro.html')

def consulta_produtos(request):

    lista_produtos = Produtos.objects.all()
    return render(request,'lista.html', {'lista_produtos':lista_produtos})

def verificar_produto(request, id):

    produto = get_object_or_404(Produtos, pk=id)
    return render(request,'info_produto.html', {'produto':produto})


