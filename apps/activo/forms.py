# coding=utf8
from django import forms
from activofijo.models import Activo

IVA = '14'

class ActivoForm(forms.ModelForm):
	
	class Meta:
		model = Activo

		fields = [
            'fotografia',
			'descripcion',
			'costo',
			'iva',
			'fecha_compra',
			'fecha_registro',
			'vida_util',
			'valor_remanente',
			'fecha_venta',
			'proveedor',
			'categoria',
			'estado',
			'condicion',
			'responsable',
		]
		labels = {
            'fotografia': 'Fotografia',
			'descripcion': 'Descripcion',
			'costo': 'Costo',
			'iva': 'I.V.A (%)',
			'fecha_compra': 'Fecha de compra',
			'fecha_registro': 'Fecha de registro',
			'vida_util': 'Tiempo de vida util (Años)',
			'valor_remanente': 'Valor remanente',
			'fecha_venta': 'Fecha de venta',
			'proveedor': 'Proveedor',
			'categoria': 'Categoria',
			'estado': 'Estado',
			'condicion': 'Condicion',
			'responsable': 'Responsable',
		}
		widgets = {
            'fotografia': forms.FileInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'costo': forms.NumberInput(attrs={'class':'form-control'}),
			'iva': forms.TextInput(attrs={'class':'form-control','value':IVA}),
			'fecha_compra': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
			'fecha_registro': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
			'vida_util': forms.NumberInput(attrs={'class':'form-control'}),
			'valor_remanente': forms.NumberInput(attrs={'class':'form-control'}),
			'fecha_venta': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
			'proveedor': forms.Select(attrs={'class':'form-control'}),
			'categoria': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'condicion': forms.Select(attrs={'class':'form-control'}),
			'responsable': forms.Select(attrs={'class':'form-control'}),
		}