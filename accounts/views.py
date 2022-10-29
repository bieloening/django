from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def logar(request):

    if request.method == 'POST':
        usuario = request.POST.get('logarUsuario')
        senha = request.POST.get('logarSenha')
        check = auth.authenticate(request, username=usuario, password=senha)

        if check is not None:
            auth.login(request, check)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos!!')
            return redirect('logar')

    else:
        return render(request, 'logar.html')

def logout(request):
    auth.logout(request)
    return redirect('logar')

def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST.get('cadastrarUsuario')
        senha = request.POST.get('cadastrarSenha')
        senha2 = request.POST.get('repetirSenha')

        

        if len(senha) < 5 or len(senha) > 12:
            messages.error(request, 'Senha deve estar entre 5 e 12')
            print("Senha deve estar entre 5 e 12")
            return redirect('cadastro')

        elif senha != senha2:
            messages.error(request, 'As senhas devem ser iguais')
            print("As senhas devem ser iguais")
            return redirect('cadastro')


        else:
            User.objects.create_user(username=usuario, password=senha)
            print("Cadastrou")
            return redirect('logar')
        

    else:
        print("atualizou a página cadastrar")

        return render(request, 'cadastrar.html')
