from django import forms
from .models import Class

class CreateClassForm(forms.ModelForm):

	class Meta:
		model = Class
		fields = ('title', 'address', 'date', 'time', 'image', 'description', 'user')
		widgets = {
			'title' : forms.TextInput(attrs = 
				{
					'type' : 'text',
					'class' : 'form-control form-control-customize-2', 
					'placeholder' : 'Title Class'
				}),
			'address' : forms.TextInput(attrs = 
				{
					'type' : 'text',
					'class' : 'form-control form-control-customize-2',
					'placeholder' : 'Address'
				}),
			'date' : forms.TextInput(attrs = 
				{
					'type' : 'date',
					'class' : 'form-control form-control-customize-2',
					'placeholder' : 'Date'
				}),
			'time' : forms.TextInput(attrs = 
				{
					'type' : 'time',
					'class' : 'form-control form-control-customize-2',
					'placeholder' : 'Time'
				}),

			'description' : forms.Textarea(attrs = 
				{ 
					'rows' : 10,
					'class' : 'form-control form-control-customize-2',
					'placeholder' : 'Description'
				})
		}