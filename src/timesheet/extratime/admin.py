# -*- coding: utf-8 -*-

from django.contrib import admin
from timesheet.extratime.models import *

class AttatchmentInline(admin.StackedInline):
    model = Attatchment

class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('type','description', )
    
class EventAdmin(admin.ModelAdmin):
    list_display = ('creator','created','description','hours', )
    inlines = [AttatchmentInline]    
    def save_model(self, request, instance, form, change):
        instance.creator = request.user
        super(EventAdmin, self).save_model(request, instance, form, change)    
    
if Event not in admin.site._registry:
    admin.site.register(Event, EventAdmin)
    
if EventType not in admin.site._registry:
    admin.site.register(EventType, EventTypeAdmin)