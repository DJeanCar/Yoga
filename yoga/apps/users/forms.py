from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User

class MyUserCreationForm(UserCreationForm):

	def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			User._default_manager.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(self.error_messages['duplicate_username'])

	class Meta(UserCreationForm.Meta):
		model = User

class UserRegistrationForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('full_name', 'email', 'password', 'location')
		widgets = {
			'full_name' : forms.TextInput(attrs = 
				{
					'type' : 'text',
					'class' : 'form-control form-control-customize-2', 
					'placeholder' : 'Full Name'
				}),
			'email' : forms.TextInput(attrs = 
				{
					'type' : 'email',
					'class' : 'form-control form-control-customize-2',
					'placeholder' : 'E-mail'
				}),
			'password' : forms.TextInput(attrs = 
				{
					'type' : 'password',
					'class' : 'form-control form-control-customize-2',
					'placeholder' : 'Password'
				}),
			'location' : forms.TextInput(attrs = 
				{
					'type' : 'text',
					'class' : 'form-control form-control-customize-2',
					'placeholder' : 'Location'
				})
		}	

class LoginForm(forms.Form):

	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput)