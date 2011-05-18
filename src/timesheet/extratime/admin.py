# -*- coding: utf-8 -*-

from django.contrib import admin
from timesheet.extratime.models import *

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('type','description', )
    
class JobAdmin(admin.ModelAdmin):
    list_display = ('creator','created','description','hours', )
    def save_model(self, request, instance, form, change):
        instance.creator = request.user
        super(JobAdmin, self).save_model(request, instance, form, change)    

class EnjoyAdmin(admin.ModelAdmin):
    list_display = ('creator','created','description','hours', )
    def save_model(self, request, instance, form, change):
        instance.creator = request.user
        super(EnjoyAdmin, self).save_model(request, instance, form, change)    
    
if Job not in admin.site._registry:
    admin.site.register(Job, JobAdmin)

if Enjoy not in admin.site._registry:
    admin.site.register(Enjoy, EnjoyAdmin)
    
if JobType not in admin.site._registry:
    admin.site.register(JobType, JobTypeAdmin)