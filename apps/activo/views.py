from django.shortcuts import render, redirect
from apps.activo.forms import ActivoForm
from apps.activo.models import Activo

# Create your views here.

def listar(request):
	activo = Activo.objects.all()
	contexto = {'activos':activo}

	return render(request, 'activo/show.html', contexto)

def crear(request):
	if request.method == 'POST':
		form = ActivoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('activo:listar')
	else:
		form = ActivoForm()

	return render(request, 'activo/form.html', {'form':form})

def editar(request, id_activo):
	activo = Activo.objects.get(id=id_activo)
	if request.method == 'GET':
		form = ActivoForm(instance=activo)
	else:
		form = ActivoForm(request.POST, instance=activo)
		if form.is_valid():
			form.save()
		return redirect('activo:listar')
	return render(request, 'activo/form.html', {'form':form})

def eliminar(request, id_activo):
	activo = Activo.objects.get(id=id_activo)
	if request.method == 'POST':
		activo.delete()
		return redirect('activo:listar')

	return render(request, 'activo/delete.html', {'activo':activo})