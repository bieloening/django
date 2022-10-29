from ast import Return
from django.shortcuts import redirect, render
from .models import Tarefas
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name= 'logar')
def index(request):

    if request.user.is_superuser:
        tarefas = Tarefas.objects.all()
        return render(request, 'index.html', {'tarefas':tarefas})

    tarefas = Tarefas.objects.filter(usuario_id=request.user.id)
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

    Tarefas.objects.create(titulo=titulo, descricao=descricao, data=data, status=status, usuario_id=request.user.id)

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


def buscar(request):
    termo = request.GET.get('termo')

    tarefas = Tarefas.objects.filter(titulo__icontains=termo)
    return render(request, 'index.html', {'tarefas':tarefas})
