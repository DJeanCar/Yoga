from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager, models.Manager):

	def _create_user(self, email, password, is_staff,
				is_superuser, **extra_fields):

		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')
		user = self.model(email=email, is_active=True,
				is_staff = is_staff, is_superuser = is_superuser, **extra_fields)
		user.set_password(password)
		user.save( using = self._db)
		return user

	def create_user(self,email, password=None, **extra_fields):
		return self._create_user(email, password, False,
				False, **extra_fields)

	def create_superuser(self, email, password=None, **extra_fields):
		return self._create_user(email, password, True,
				True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

	email = models.EmailField(unique = True)
	full_name = models.CharField(max_length = 150)
	location = models.CharField(max_length = 100)
	avatar = models.ImageField(upload_to = 'users', null=True, blank=True)
	teacher = models.BooleanField(default = False)
	student = models.BooleanField(default = False)
	premium = models.BooleanField(default = False)

	objects = UserManager()

	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_short_name(self):
		return self.full_name