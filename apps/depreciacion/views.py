from django.shortcuts import render
from activofijo.models import Depreciacion, Activo
import datetime
from django.utils.timesince import timesince

# Create your views here.
def listar(request):
	depreciacion = Depreciacion.objects.all()

	for dep in depreciacion:
		activo = Activo.objects.get(id=dep.activo.id)
		dep.valor_depreciado = float(activo.costo / activo.vida_util)
		dep.fecha_inicio = activo.fecha_compra
		fecha_inicio = dep.fecha_inicio
		dep.fecha_fin = (fecha_inicio + datetime.timedelta(activo.vida_util*365)).isoformat()
		dep.fecha_fin = datetime.datetime.strptime(dep.fecha_fin, "%Y-%m-%d").date()
		dep.depreciacion_acumulada = time_until(dep.fecha_inicio.year) * round(float(dep.valor_depreciado), 2)
		dep.save()
	
	contexto = {'depreciaciones':depreciacion}

	return render(request, 'depreciacion/show.html', contexto)

def time_until(value):
    now = datetime.datetime.now().year
    try:
        difference = now - value
        print difference
    except:
        return value

    return difference