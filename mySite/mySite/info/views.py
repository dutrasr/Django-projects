from django.shortcuts import render

# Create your views here.
from .models import Info, Skill, Social
from datetime import date

def home(request):

	todayDate = date.today()

	infos = Info.objects.get()
	socials = Social.objects.all()
	skills = Skill.objects.all()
	context = {
		'infos': infos,
		'todayDate': todayDate,
		'skills': skills,
		'socials': socials,
	}

	return render(request, 'home.html', context)