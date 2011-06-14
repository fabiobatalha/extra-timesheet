from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
    
EVENT_TYPE = [("enjoy","enjoy"),("overtime","overtime")]
    
class EventType(models.Model):
    name = models.CharField(_('Event Type Name'), db_index=True, max_length=128 )
    description = models.TextField(_('Event Type Description'),)
    type = models.CharField(_('Event Type'),choices=EVENT_TYPE, max_length='16')
    
    def __unicode__(self):
        return u'%s' % (self.name)    

class Event(models.Model):
    class Meta:
        ordering = ['-created']
    creator = models.ForeignKey(User, related_name='event_creator', editable=False)
    created = models.DateTimeField(_('Date of Registration'),default=datetime.now,
        editable=False)
    type = models.ForeignKey(EventType, related_name='event_type', db_index=True)
    description = models.TextField(_('Event Description'),)
    hours = models.IntegerField(_('Hours in Job'),)
    validated = models.BooleanField(_('Validated Job'),)
    validated_by = models.ForeignKey(User, related_name='overtime_validated_by')    
    
class Attatchment(models.Model):
    file = models.FileField(_('Upload File'), blank=True,
        upload_to='static', )
    attatch = models.ForeignKey(Event, related_name="event_attatch", null=True,
        blank=True,  )