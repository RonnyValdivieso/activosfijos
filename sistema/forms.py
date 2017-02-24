from django import forms
from sistema.models import Activo

class ActivoForm(forms.ModelForm):
	
	class Meta:
		model = Activo

		fields = [
			'descripcion',
			'costo',
			'iva',
			'fecha_compra',
			'fecha_registro',
			'vida_util',
			'valor_remanente',
			'fotografia',
			'fecha_venta',
			'proveedor',
			'categoria',
			'estado',
			'condicion',
			'responsable',
		]
		labels = {
			'descripcion': 'Descripcion',
			'costo': 'Costo',
			'iva': 'I.V.A',
			'fecha_compra': 'Fecha de compra',
			'fecha_registro': 'Fecha de registro',
			'vida_util': 'Vida util',
			'valor_remanente': 'Valor remanente',
			'fotografia': 'Fotografia',
			'fecha_venta': 'Fecha de venta',
			'proveedor': 'Proveedor',
			'categoria': 'Categoria',
			'estado': 'Estado',
			'condicion': 'Condicion',
			'responsable': 'Responsable',
		}
		widgets = {
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'costo': forms.NumberInput(attrs={'class':'form-control'}),
			'iva': forms.NumberInput(attrs={'class':'form-control'}),
			'fecha_compra': forms.DateInput(attrs={'class':'form-control'}),
			'fecha_registro': forms.DateInput(attrs={'class':'form-control'}),
			'vida_util': forms.NumberInput(attrs={'class':'form-control'}),
			'valor_remanente': forms.NumberInput(attrs={'class':'form-control'}),
			'fotografia': forms.FileInput(attrs={'class':'form-control'}),
			'fecha_venta': forms.DateInput(attrs={'class':'form-control'}),
			'proveedor': forms.Select(attrs={'class':'form-control'}),
			'categoria': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'condicion': forms.Select(attrs={'class':'form-control'}),
			'responsable': forms.Select(attrs={'class':'form-control'}),
		}