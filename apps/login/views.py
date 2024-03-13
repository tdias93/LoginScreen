from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from apps.login.forms import LoginForms

def index(request):
    return

def login_view(request):

    # INSTANCIA O FORMULARIO
    form = LoginForms()

    # VALIDA SE O USUÁRIO JÁ ESTÁ LOGADO
    if request.user.is_authenticated:
            
            # DIRECIONA PARA PAGINA ADMIN.
            return redirect(reverse('admin:index')) 

    # VALIDA SE A REQUISIÇÃO É DO TIPO POST
    if request.method == 'POST':

        # INSTANCIA O FORMULARIO COM DADOS DA REQUISIÇÃO
        form = LoginForms(request.POST)

        # VALIDA SE O FORMULARIO ESTÁ VALIDADO
        if form.is_valid():
            
            # PEGA DADOS DO FORMULARIO
            username = form.cleaned_data.get('username')     # PEGA DADOS DO USUÁRIO NO FORMULARIO
            password = form.cleaned_data.get('password')     # PEGA DADOS DA SENHA NO FORMULARIO

            try:

                # PEGA DADOS DO USUÁRIO NO BD
                user = User.objects.get(username=username)   

                # VALIDA SE O USUÁRIO ESTÁ ATIVO
                if not user.is_active:

                    # GERA MENSSAGEM DE ERRO
                    form.add_error('username', 'Usuário Bloqueado.')   
                
                else:
                    # REALIZA A AUTENTICAÇÃO DO USUÁRIO
                    user = auth.authenticate(username=username, password=password)

                    # VALIDA SE O USUÁRIO FOI AUTENTICADO
                    if user is not None:

                        auth.login(request, user)                 # RELIZA O LOGIN
                        return redirect(reverse('admin:index'))   # DIRECIONA PARA PAGINA ADMIN
                    
                    else:

                        # GERA MENSSAGEM DE ERRO
                        form.add_error('password', 'Senha Incorreta')   

            except User.DoesNotExist:

                # GERA MENSSAGEM DE ERRO
                form.add_error('username', 'Usuário não Cadastrado.')   
 
    return render(request, 'login/login.html', {'form': form})