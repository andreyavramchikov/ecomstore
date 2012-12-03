from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from django.views.static import * 
from django.conf import settings


urlpatterns = patterns('',
   (r'^catalog/$', 'preview.views.home'),
   (r'^admin/', include(admin.site.urls)),   
   (r'^$', 'catalog.views.index'),
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   (r'^category/(?P<category_slug>[-\w]+)/$','catalog.views.show_category'),
   (r'^product/(?P<product_slug>[-\w]+)/$','catalog.views.show_product'),

)
