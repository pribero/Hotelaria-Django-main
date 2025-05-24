from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import *

# Create your views here.
def Homepage(request):
    context = {}
    dados_home = homepage.objects.all()
    context['dados_home'] = dados_home
    return render(request, 'homepage.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        
        else:
            context = {
                "alerta" : "Usuário ou Senha Invalida"
            }
            return render(request, 'Login.html', context)

    else:
        return render(request, 'Login.html')
    
    
@login_required(login_url='/') 
def addQuarto(request):
    if request.method == 'POST':
        form = quartoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_quartin')
    else:
        form = quartoForms()

    context = {'form': form}
    return render(request, 'addQuartos.html', context)

    
@login_required(login_url='/') 
def addColabo(request):
    if request.method == 'POST':
        form = AtendenteForms(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user.groups.clear()
            grupo = Group.objects.get(name='Atendente')
            user.groups.add(grupo)

            messages.success(request, 'Atendente cadastrado com sucesso!')
            return redirect('addColabo')
    else:
        form = AtendenteForms()
    return render(request, 'addColabos.html', {'form': form})

@login_required(login_url='/')  
def reserva(request):
    context = {}
    return render(request, 'reservas.html', context)

@login_required(login_url='/')
def listar_quartin(request, tipo_quarto=None):

    if tipo_quarto:
        quartin = quarto.objects.filter(tipo=tipo_quarto)
    else:
        quartin = quarto.objects.all()

    context = {
        'quartos': quartin,
        'tipo_selecionado': tipo_quarto,
    }

    return render(request, 'listar_quartin.html', context)

@login_required(login_url='/')
def editar_quartin(request, id):
    quarto_editar = quarto.objects.get(id=id)
    
    if request.method == 'POST':
        form = quartoForms(request.POST, request.FILES, instance=quarto_editar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quarto editado com sucesso!')
            return redirect('listar_quartin')
    else:
        form = quartoForms(instance=quarto_editar)

    context = {'form': form}
    return render(request, 'editar_quartin.html', context)

@login_required(login_url='/')
def addHospede(request):
    if request.method == 'POST':
        pass

def Sair(request):
    logout(request)
    return redirect ('homepage')

