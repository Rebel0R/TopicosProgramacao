from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from appPythonWeb.form import CarrosForm
from appPythonWeb.models import Carros
#from django.http import HttpResponse


# Create your views here.
def home(request):
    dados = {}
    dados['db'] = Carros.objects.all()
    return render(request, "index.html", dados)
 #   return HttpResponse("Olá mundo!")
    #return render(request, "formulario.html")

def formulario(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, "formulario.html", data)

def inserir(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def visualizar(request, pk):
    dados={}
    dados['db'] = Carros.objects.get(pk = pk)
    return render(request, "visualizar.html", dados)

def editar(request, pk):
    dados={}
    dados['db'] = Carros.objects.get(pk=pk)
    dados['form'] = CarrosForm(instance=dados['db'])
    return render(request, "formulario.html", dados)

def updateBD(request, pk):
    dados = {}
    dados['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=dados['db'])
    if form.is_valid():
        form.save()
        return render(request, 'home')

def excluir(request, pk):
    dado = get_object_or_404(Carros, pk=pk)
    dado.delete()
    return redirect('home')
