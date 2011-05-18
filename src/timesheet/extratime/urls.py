from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail, object_list
from extratime.models import *
from extratime.views import *


urlpatterns = patterns('',
#    url(r'^$', user_index, name="extratime.user_index"),
#    url(r'^list/$', object_list, info_dict, name="extratime.list"),
#    url(r'^list_waiting/$', waiting_acceptance, name="extratime.waiting_acceptance"),
#    url(r'^history/(?P<object_id>\d+)/$', object_detail, info_dict, name='extratime.history' ),
#    url(r'^open/(?P<context>\w+)/(?P<type>\w+)/$', open_extratime, name='extratime.open' ),
#    url(r'^reopen/(?P<object_id>\d+)/$', reopen_extratime, name='extratime.reopen' ),
#    url(r'^resolve/(?P<object_id>\d+)/$', resolve_extratime, name='extratime.resolve' ),
#    url(r'^accept/(?P<object_id>\d+)/$', accept_extratime, name='extratime.accept' ),
#    url(r'^close/(?P<object_id>\d+)/$', close_extratime, name='extratime.close' ),
#    url(r'^newiteration/(?P<object_id>\d+)/$', new_iteration, name='extratime.new_iteration' ),
)
