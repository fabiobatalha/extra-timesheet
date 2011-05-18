from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

class Enjoy(models.Model):
    class Meta:
        ordering = ['-created']
    creator = models.ForeignKey(User, related_name='enjoy_creator', editable=False)
    created = models.DateTimeField(_('Date of Registration'),default=datetime.now,
        editable=False)
    description = models.TextField(_('Enjoying Description'),)
    hours = models.IntegerField(_('Hours Enjoying'),)
    validated = models.BooleanField(_('Validated Job'),)
    validated_by = models.ForeignKey(User, related_name='enjoy_validated_by')

class JobType(models.Model):
    type = models.CharField(_('Job Type'), db_index=True, max_length=128 )
    description = models.TextField(_('Job Type Description'),)
    
    def __unicode__(self):
        return u'%s' % (self.type)    

class Job(models.Model):
    class Meta:
        ordering = ['-created']
    creator = models.ForeignKey(User, related_name='job_creator', editable=False)
    created = models.DateTimeField(_('Date of Registration'),default=datetime.now,
        editable=False)
    type = models.ForeignKey(JobType, related_name='job_type', db_index=True)
    description = models.TextField(_('Job Description'),)
    attachments = models.FileField(_('Upload File'), blank=True,
        upload_to='files', )
    hours = models.IntegerField(_('Hours in Job'),)
    validated = models.BooleanField(_('Validated Job'),)
    validated_by = models.ForeignKey(User, related_name='job_validated_by')    

class Attatchment(models.Model):
    job = models.ForeignKey(Job, related_name="job_attatch", null=True,
        blank=True, db_index=True, )
    file = models.FileField(_('Upload File'), blank=True,
        upload_to='static', )
