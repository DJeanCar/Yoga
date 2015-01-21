from django.conf.urls import patterns, url
from .views import CreateClassView, HomeView, AboutView, ProfilesView, ResourcesView, CalendarView, DonateView

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view()),
	url(r'^about/$', AboutView.as_view()),
	url(r'^profiles/$', ProfilesView.as_view()),
	url(r'^resources/$', ResourcesView.as_view()),
	url(r'^calendar/$', CalendarView.as_view()),
	url(r'^post-class/$', CreateClassView.as_view()),
	url(r'^donate/$', DonateView.as_view()),
)
