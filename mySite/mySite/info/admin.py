from django.contrib import admin

# Register your models here.
from .models import Skill, Info, Social

class SkillAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'porcentage', 'time_Stamp', 'updated']

class InfoAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'email', 'phone', 'city', 'state', 'country']

class SocialAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'show']


admin.site.register(Skill, SkillAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(Social, SocialAdmin)