from django.db import models
from apps.users.models import User

class Class(models.Model):

	user = models.ForeignKey(User, null = True, blank = True)
	title = models.CharField(max_length=200)
	description = models.TextField()
	address = models.CharField(max_length=200)
	image = models.ImageField(upload_to = 'classes', null=True, blank=True)
	date = models.DateField()
	time = models.TimeField()

	def __unicode__(self):
		return self.title