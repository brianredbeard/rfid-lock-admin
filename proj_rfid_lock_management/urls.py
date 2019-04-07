from django.conf import settings
from django.urls import include, path, re_path
import django.contrib.auth.urls


from django.views.generic import TemplateView
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
   path('admin/', include('django.contrib.auth.urls')),
   #path(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset',
   #    name='admin_password_reset'),
   #path(r'^admin/password_reset/done/$',
   #    'django.contrib.auth.views.password_reset_done'),
   #path(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
   #    'django.contrib.auth.views.password_reset_confirm'),
   #path(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

   # go directly to the admin page for the *application*
   re_path(r'^lockadmin/', admin.site.urls),

   # keycard activation
   re_path(r'start_scan/(?P<lockuser_object_id>\d+)/$',
       initiate_new_keycard_scan),
   re_path(r'done_scan/(?P<new_scan_pk>\d+)/$',
       finished_new_keycard_scan),

   # Highchart of visitors
   re_path(r'^chart/', chartify),

   # keycard authentication
   re_path(r'checkdoor/(?P<doorid>\d+)/checkrfid/(?P<rfid>\w{10})/$',
       check),

   # Arduino requesting list of all allowed RFIDs for
   # specified door
   re_path(r'door/(?P<doorid>\d+)/getallowed/$',
       get_allowed_rfids),

   # Uncomment the admin/doc line below to enable admin documentation:
   # path(r'^admin/doc/',
   # include('django.contrib.admindocs.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
