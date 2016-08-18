# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2016-07-29 21:04:07
# @Last Modified by:   dutrasr
# @Last Modified time: 2016-08-16 03:47:23

from django.shortcuts import render

def home(request):

	return render(request, 'home2.html', {})