from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import MyUserCreationForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

	pass

	# add_form = MyUserCreationForm
	# list_display = ('email', 'full_name')
	# search_fields = ('email',)
	# list_filter = ('is_superuser',)
	# ordering = ('email',)
	# filter_horizontal = ('groups', 'user_permissions')

	# fieldsets = (
	# 		('User', {'fields' : ('email', 'password')}),
	# 		('Personal Info', {'fields' : (
	# 						'full_name',
	# 						'avatar',
	# 						'location',
	# 						'teacher',
	# 						'student',
	# 						'premium',
	# 				)}),
	# 		('Permissions', {'fields': (
	# 						'is_active',
	# 						'is_staff',
	# 						'is_superuser',
	# 						'groups',
	# 						'user_permissions',
	# 			)}),
	# 	)