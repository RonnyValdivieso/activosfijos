from django.shortcuts import render
from activofijo.models import Depreciacion

# Create your views here.
def listar(request):
	depreciacion = Depreciacion.objects.all()
	contexto = {'depreciaciones':depreciacion}

	return render(request, 'depreciacion/show.html', contexto)