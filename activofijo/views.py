from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	#return HttpResponse('Index')
	return render(request, 'activo/index.html')