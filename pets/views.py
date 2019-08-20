from django.shortcuts import render
from .models import Pessoa
from django.core.files.storage import FileSystemStorage

def mostrar_pessoas(request):
  pessoa = Pessoa.objects.all()


  return render(request, 'index.html' , {'dados': pessoa})

def mostrar_formulario_cadastro(request):

  if request.method == 'POST':

    pessoa = Pessoa()
    fs = FileSystemStorage()

    pessoa.nome = request.POST.get('nome')
    pessoa.cidade = request.POST.get('cidade')
    pessoa.email = request.POST.get('email')
    pessoa.telefone = request.POST.get('telefone')
    pessoa.genero = request.POST.get('genero')
    pessoa.especie = request.POST.get('especie')
    pessoa.foto = request.FILES['foto']
    pessoa.desc = request.POST.get('desc')

    
    name = fs.save(pessoa.foto.name, pessoa.foto)
    url = fs.url(name)

    pessoa.url = url

    pessoa.save()
    
  return render(request, 'pets.html')