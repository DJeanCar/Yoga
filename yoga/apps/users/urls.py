from django.conf.urls import patterns, url
from .views import RegisterUserView, LoginUserView, PremiumUserView, ProfileUserView, EditProfileUserView, RegainAccessUserView

urlpatterns = patterns('',
	url(r'^register/$', RegisterUserView.as_view()),
	url(r'^login/$', LoginUserView.as_view()),
	url(r'^logout/$', 'apps.users.views.LogOut'),
	url(r'^premium/$', PremiumUserView.as_view()),
	url(r'^profile/$', ProfileUserView.as_view()),
	url(r'^edit/$', EditProfileUserView.as_view()),
	url(r'^regain-access/$', RegainAccessUserView.as_view()),

	url(r'^paypal/create/$', 'apps.users.paypal.paypal_create', name="create"),
	url(r'^paypal/execute/$', 'apps.users.paypal.paypal_execute', name="execute"),

)
