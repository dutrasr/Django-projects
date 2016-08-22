# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2016-08-19 02:56:02
# @Last Modified by:   dutrasr
# @Last Modified time: 2016-08-19 02:57:01

from django.shortcuts import render

def home(request):

	return render(request, 'home.html', {})