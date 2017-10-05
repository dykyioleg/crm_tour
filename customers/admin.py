from django.contrib import admin
from .models import *


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Customer._meta.fields]
	
	class Meta:
		model = Customer

admin.site.register(Customer,CustomerAdmin)



class PhoneAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Phone._meta.fields]
	
	class Meta:
		model = Phone

admin.site.register(Phone,PhoneAdmin)



class FamilyAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Family._meta.fields]
	
	class Meta:
		model = Family

admin.site.register(Family,FamilyAdmin)