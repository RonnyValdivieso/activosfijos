from django.shortcuts import render, redirect
from apps.activo.forms import ActivoForm
from apps.activo.models import Activo

# Create your views here.

def index(request):
	return render(request, 'activo/index.html')

def activo_mostrar(request):
	activo = Activo.objects.all()
	contexto = {'activos':activo}

	return render(request, 'activo/show.html', contexto)

def activo_nuevo(request):
	if request.method == 'POST':
		form = ActivoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/activo/show.html')
	else:
		form = ActivoForm()

	return render(request, 'activo/form.html', {'form':form})

def activo_editar(request, id_activo):
	activo = Activo.objects.get(id=id_activo)
	if request.method == 'GET':
		form = ActivoForm(instance=activo)
	else:
		form = ActivoForm(request.POST, instance=activo)
		if form.is_valid():
			form.save()
		return redirect('/activo/show.html')
	return render(request, '/activo/form.html', {'form':form})