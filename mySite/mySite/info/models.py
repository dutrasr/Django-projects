from django.db import models
# Create your models here.
class Skill(models.Model):
	"""Skills db."""

	skill_Name	= models.CharField(max_length=20, blank=True, null=True)
	porcentage	= models.IntegerField(default=0, blank=True, null=True)
	image_Link	= models.CharField(max_length=120, blank=True, null=True)
	time_Stamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated		= models.DateTimeField(auto_now_add=False, auto_now=True)
	#email		= models.EmailField()
	#phoneRegex	= RegexValidator(regex=r'^\+\d{8,15}$', message="Phone number must be in the format: '+999999999999'. Up to 15digits.")
	#phone		= models.CharField(validators=[phoneRegex], blank=True)

	def __str__(self):
		return self.skill_Name

class Info(models.Model):
	"""Infos db."""

	name		= models.CharField(max_length=20, blank=True, null=True)
	email		= models.EmailField()
	phone		= models.CharField(max_length=16, blank=True, null=True)
	profession	= models.CharField(max_length=20, blank=True, null=True)
	intro		= models.TextField(blank=True, null=True)
	city		= models.CharField(max_length=20, blank=True, null=True)
	state		= models.CharField(max_length=20, blank=True, null=True)
	country		= models.CharField(max_length=20, blank=True, null=True)
	time_Stamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated		= models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __str__(self):
		return self.name

class Social(models.Model):
	"""Social db."""

	name		= models.CharField(max_length=20, blank=True, null=True)
	link		= models.URLField(max_length=250, blank=True, null=True)
	image_Link	= models.CharField(max_length=120, blank=True, null=True)
	show		= models.BooleanField(default=False)
	time_Stamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated		= models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __str__(self):
		return self.name