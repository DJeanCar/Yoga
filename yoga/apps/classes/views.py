from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from braces.views import LoginRequiredMixin

from .forms import CreateClassForm

class HomeView(TemplateView):

	template_name = 'classes/home.html'

class CreateClassView(LoginRequiredMixin, CreateView):

	form_class = CreateClassForm
	template_name = 'classes/create_class.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateClassView, self).form_valid(form)