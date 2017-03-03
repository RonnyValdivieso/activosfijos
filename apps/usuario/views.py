from django.shortcuts import render
from django.contrib.auth.models import User
from activofijo.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import RegistroForm

# Create your views here.
class RegistroUsuario(CreateView):
	model = User
	template_name = 'usuario/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('activo:listar')