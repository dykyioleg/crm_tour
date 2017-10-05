from django.db import models
from customers.models import Customer
from tours.models import Tour

# Create your models here.

class StatusPayment(models.Model):
	name = models.CharField(max_length=40,blank=True,null=True,default=None)
	is_paid = models.BooleanField(default=True)
	half_paid = models.BooleanField(default=True)
	is_reserved = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		verbose_name='StatusPayment'
		verbose_name_plural='StatusPayments'


	def __str__(self):
		return " {0}".format(self.name)


class Order(models.Model):
	customer = models.ForeignKey(Customer,blank=True,null=True,default=None)
	tour = models.ForeignKey(Tour,blank=True,null=True,default=None)
	nmb_tours = models.IntegerField(default=0)
	status_payment = models.ForeignKey(StatusPayment,blank=True,null=True,default=None)
	total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	datetime = models.DateTimeField(auto_now_add=True,auto_now=False)



	class Meta:
		verbose_name = "Order"
		verbose_name_plural = "Orders"

	def __str__(self):
		return "{0} - {1}".format(self.customer,self.tour)
    
	def save(self,*args,**kwargs):
		self.total_price = int(self.nmb_tours)*self.tour.total_price

		super(Order,self).save(*args,**kwargs)