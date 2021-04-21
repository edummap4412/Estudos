from django.shortcuts import render

from .models import Produto, Costumer


def conteudo(request):
    costumer = Costumer.objects.all()
    context = {
        'Conteudo': 'Retificando conhecimentos',
         'costumers': costumer

    }
    return render(request, 'conteudo.html', context)


def index(request):
    produto = Produto.objects.all()

    print(dir(request.user))
    print(f"USER:{request.user}")

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário LOGADO'
    context = {
        'Intro': 'Introduzindo Página para testes',
        'logado': teste,
        'produtos': produto
    }
    return render(request, 'index.html', context)


def produto(request,id):
    prod = Produto.objects.get(id=id)
    context = {
        'produto':prod
    }
    return render(request, 'produto.html',context)
