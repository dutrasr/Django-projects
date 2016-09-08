# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2016-09-08 03:23:38
# @Last Modified by:   dutrasr
# @Last Modified time: 2016-09-08 03:43:13

from django.db import models

class info(models.Model):
	"""Database for generic infos."""

	name		= models.CharField(max_length=120, blank=True, null=True)
	email		= models.EmailField()
	phoneRegex	= RegexValidator(regex=r'^\+\d{8,15}$', message="Phone number must be in the format: '+999999999999'. Up to 15digits.")
	phone		= models.CharField(validators=[phoneRegex], blank=True)
	timeStamp 	= models.DateTimeField(auto_now_add=True, auto_now=False)
	updated		= models.DateTimeField(auto_now_add=False, auto_now=True)