# -*- coding: utf-8 -*-
# @Author: dutrasr
# @Date:   2016-07-29 21:04:07
# @Last Modified by:   dutrasr
# @Last Modified time: 2016-09-12 04:16:13

from django.shortcuts import render
"""from datetime import date

from .models import Info

def getData(var):
	if var == 'skills':
		skills = [
			['python', 70],
			['django', 50],
			['mongodb', 30],
			['html5', 50],
			['css3', 50],
			['git', 60],
			['node', 0]]
		return skills

	if var == 'socials':
		socials = [
			['facebook', 'https://www.facebook.com/rafael.dutra.94009', True],
			['github-alt', 'https://github.com/dutrasr', True],
			['linkedin', 'https://www.linkedin.com/in/rafael-dutra-1bb140b7', True],
			['stack-overflow', 'https://stackoverflow.com/users/2444285/dutrasr', False]]
		return socials

def getDate():
	return date.today()


def home(request):

	todayDate = getDate()
	skills = getData('skills')
	socials = getData('socials')
	infos = getData('infos')



	context = {
		'todayDate': todayDate,
		'skills': skills,
		'socials': socials,
		'email': 'dutrasr@gmail.com',
		'phone': [53, 81587556],
		'location': ['Pelotas', 'RS', 'Brazil'],
	}

	return render(request, 'home.html', context)"""