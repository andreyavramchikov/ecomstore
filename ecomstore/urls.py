from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^catalog/$', 'preview.views.home'),
   (r'^admin/', include(admin.site.urls)),
)
