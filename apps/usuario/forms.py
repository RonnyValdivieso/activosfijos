# coding=utf8
from django import forms
from activofijo.models import Usuario

class UsuarioForm(forms.ModelForm):
	
	class Meta:
		model = Usuario

		fields = [
            'user',
			'pass_field',
			'tipo_usuario',
			'persona',

		]
		labels = {
            'user': 'Usuario',
			'pass_field': 'Contraseña',
			'tipo_usuario': 'Tipo de usuario',
			'persona': 'Persona',
		}
		widgets = {
			'user': forms.TextInput(attrs={'class':'form-control'}),
			'pass_field': forms.PasswordInput(attrs={'class':'form-control'}),
			'tipo_usuario': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.TextInput(attrs={'class':'form-control'}),
		}