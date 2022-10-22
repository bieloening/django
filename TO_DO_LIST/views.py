from ast import Return
from django.shortcuts import redirect, render
from .models import Tarefas
from django.contrib import auth

def index(request):
    tarefas = Tarefas.objects.all()
    return render(request, 'index.html', {'tarefas':tarefas})

def adicionar(request):
    return render(request, 'adicionar.html')


def adicionar_tarefa(request):
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    data = request.POST.get('data')
    status = request.POST.get('status')

    if status == 'Pendente':
        status = False

    else:
        status = True

    Tarefas.objects.create(titulo=titulo, descricao=descricao, data=data, status=status)

    return redirect('home')

def deletar(request, id):
    Tarefas.objects.get(id=id).delete()
    

    return redirect('home')

def finalizar(requets, id):
    item = Tarefas.objects.get(id=id)
    item.status = True
    item.save()
    return redirect('home')

def editar(request, id):

    item = Tarefas.objects.get(id=id)

    if request.method == 'POST':

        item = Tarefas.objects.get(id=id)
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        status = request.POST.get('status')

        if status == 'Pendente':
            status = False
        else:
            status = True

        item.titulo = titulo
        item.descricao = descricao
        item.data = data
        item.status = status

        item.save()
        return redirect('home')

    else:
        return render(request, 'editar.html', {'item' :item})


def logar(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        check = auth.authenticate(request, username=usuario, password=senha)

        if check is not None:
            auth.login(request, check)
            return redirect('home')
        else:
            return redirect('login')

    else:
        return render(request, 'logar.html')