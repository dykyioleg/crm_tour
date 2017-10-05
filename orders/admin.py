from django.contrib import admin
from .models import *

# Register your models here.

class StatusPaymentAdmin(admin.ModelAdmin):
	list_display = [field.name for field in StatusPayment._meta.fields]
	
	class Meta:
		model = StatusPayment

admin.site.register(StatusPayment,StatusPaymentAdmin)


class OrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Order._meta.fields]
	
	class Meta:
		model = Order

admin.site.register(Order,OrderAdmin)

