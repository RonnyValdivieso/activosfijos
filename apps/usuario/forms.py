# coding=utf8
from django import forms
from activofijo.models import Usuario

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'email': 'Correo electrónico',
		}

# class UsuarioForm(forms.ModelForm):
	
# 	class Meta:
# 		model = Usuario

# 		fields = [
#             'user',
# 			'pass_field',
# 			'tipo_usuario',
# 			'persona',

# 		]
# 		labels = {
#             'user': 'Usuario',
# 			'pass_field': 'Contraseña',
# 			'tipo_usuario': 'Tipo de usuario',
# 			'persona': 'Persona',
# 		}
# 		widgets = {
# 			'user': forms.TextInput(attrs={'class':'form-control'}),
# 			'pass_field': forms.PasswordInput(attrs={'class':'form-control'}),
# 			'tipo_usuario': forms.TextInput(attrs={'class':'form-control'}),
# 			'persona': forms.TextInput(attrs={'class':'form-control'}),
# 		}