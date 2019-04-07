from django.views.generic import TemplateView
from django.conf.urls import url, include
from rfid_lock_management.models import RFIDkeycard, Door
from rfid_lock_management.views import *
from django.http import HttpResponse
from django.shortcuts import redirect

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
   # Password-reset: add "Forgotten your password?" link on
   # log-in page
   url('^', include('django.contrib.auth.urls')),
   #url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset',
   #    name='admin_password_reset'),
   #url(r'^admin/password_reset/done/$',
   #    'django.contrib.auth.views.password_reset_done'),
   #url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
   #    'django.contrib.auth.views.password_reset_confirm'),
   #url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

   # go directly to the admin page for the *application*
   url(r'^lockadmin/', admin.site.urls),

   # keycard activation
   url(r'start_scan/(?P<lockuser_object_id>\d+)/$',
       initiate_new_keycard_scan),
   url(r'done_scan/(?P<new_scan_pk>\d+)/$',
       finished_new_keycard_scan),

   # Highchart of visitors
   url(r'^chart/', chartify),

   # keycard authentication
   url(r'checkdoor/(?P<doorid>\d+)/checkrfid/(?P<rfid>\w{10})/$',
       check),

   # Arduino requesting list of all allowed RFIDs for
   # specified door
   url(r'door/(?P<doorid>\d+)/getallowed/$',
       get_allowed_rfids),

   # Uncomment the admin/doc line below to enable admin documentation:
   # url(r'^admin/doc/',
   # include('django.contrib.admindocs.urls')),
]
