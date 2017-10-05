from django.db import models

# Create your models here.

class Customer(models.Model):
	first_name = models.CharField(max_length=20,blank=True,null=True,default=None)
	last_name = models.CharField(max_length=20,blank=True,null=True,default=None)
	age = models.CharField(max_length=10,blank=True,null=True,default=None)
	email = models.EmailField(blank=True,null=True,default=None)
	city_residence = models.CharField(max_length=20,blank=True,null=True,default=None)
	address = models.CharField(max_length=20,blank=True,null=True,default=None)


	class Meta:
		verbose_name='Client'
		verbose_name_plural='Clients'

	def __str__(self):
		return "Client {0} {1}".format(self.last_name,self.first_name)


class Phone(models.Model):
	customer = models.ForeignKey(Customer,blank=True,null=True,default=None)
	phone = models.CharField(max_length=50,blank=True,null=True,default=None)


	class Meta:
		verbose_name = "Phone"
		verbose_name_plural = "Phones"

	def __str__(self):
		return "{0}".format(self.phone)



class Family(models.Model):
	customer = models.ForeignKey(Customer,blank=True,null=True,default=None)
	status = models.CharField(max_length=20,blank=True,null=True,default=None)
	first_name = models.CharField(max_length=20,blank=True,null=True,default=None)
	last_name = models.CharField(max_length=20,blank=True,null=True,default=None)
	age = models.CharField(max_length=10,blank=True,null=True,default=None)

	class Meta:
		verbose_name='Family'
		verbose_name_plural='Familys'


	def __str__(self):
		return " {0} {1}".format(self.status,self.first_name)