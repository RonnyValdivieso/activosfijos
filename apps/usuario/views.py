from django.shortcuts import render, redirect
from apps.usuario.forms import UsuarioForm
from activofijo.models import Usuario
#from django.contrib

# Create your views here.
def listar(request):
	usuario = Usuario.objects.all()
	contexto = {'usuarios':usuario}

	return render(request, 'usuario/show.html', contexto)

def crear(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('usuario:listar')
	else:
		form = UsuarioForm()

	return render(request, 'usuario/form.html', {'form':form})

def editar(request, id_usuario):
	usuario = Usuario.objects.get(id=id_usuario)
	if request.method == 'GET':
		form = UsuarioForm(instance=usuario)
	else:
		form = UsuarioForm(request.POST, instance=usuario)
		if form.is_valid():
			form.save()
		return redirect('usuario:listar')
	return render(request, 'usuario/form.html', {'form':form})

def eliminar(request, id_usuario):
	usuario = Usuario.objects.get(id=id_usuario)
	if request.method == 'POST':
		usuario.delete()
		return redirect('usuario:listar')

	return render(request, 'usuario/delete.html', {'usuario':usuario})