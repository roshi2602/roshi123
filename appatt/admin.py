from django.contrib import admin
from appatt.models import *

class ProfileAdmin(admin.ModelAdmin):
	list_dis=['user','designation','signin_time','signout_time']


admin.site.register(Profile, ProfileAdmin)