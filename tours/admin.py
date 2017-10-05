from django.contrib import admin
from .models import *

# Register your models here.

class TourAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Tour._meta.fields]
	
	class Meta:
		model = Tour

admin.site.register(Tour,TourAdmin)


class PeriodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Period._meta.fields]
	
	class Meta:
		model = Period

admin.site.register(Period,PeriodAdmin)