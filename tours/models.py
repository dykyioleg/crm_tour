from django.db import models

# Create your models here.
class Period(models.Model):
	high = models.DecimalField(max_digits=10,decimal_places=2,default=90) 
	medium = models.DecimalField(max_digits=10,decimal_places=2,default=75)
	low = models.DecimalField(max_digits=10,decimal_places=2,default=60)
	high_period = models.BooleanField(default=False)
	medium_period = models.BooleanField(default=False)
	low_period = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Period"
		verbose_name_plural = "Periods"

	def __str__(self):
		return "{0}".format('period')


class Tour(models.Model):
	country = models.CharField(max_length=20,blank=True,null=True,default=None)
	city =  models.CharField(max_length=20,blank=True,null=True,default=None)
	hotel = models.CharField(max_length=20,blank=True,null=True,default=None)
	period = models.ForeignKey(Period,blank=True,null=True,default=None)
	nmb_days = models.IntegerField(default=0)
	price_per_one_day = models.DecimalField(max_digits=10,decimal_places=2,default=0)
	total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

	class Meta:
		verbose_name = "Tour"
		verbose_name_plural = "Tours"

	def __str__(self):
		return '{0},{1}'.format(self.country,self.city)
    

	def save(self,*args,**kwargs):
		if self.period.high_period:
			self.price_per_one_day = self.period.high
		if self.period.medium_period:
			self.price_per_one_day = self.period.medium	
		if self.period.low_period:
			self.price_per_one_day = self.period.low	

		self.total_price = int(self.nmb_days)*self.price_per_one_day

		super(Tour,self).save(*args,**kwargs)