from django.conf.urls import patterns, url
from .views import CreateClassView, HomeView

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view()),
	url(r'^post-class/$', CreateClassView.as_view()),
)
