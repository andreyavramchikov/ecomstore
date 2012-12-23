from django.conf.urls.defaults import *
from ecomstore import settings

urlpatterns = patterns('accounts.views',
    (r'^register/$', 'register',
        {'template_name': 'registration/register.html' },'register'),
    (r'^my_account/$', 'my_account',{'template_name': 'registration/my_account.html'}, 'my_account'),
)
urlpatterns += patterns('django.contrib.auth.views',
    (r'^login/$', 'login',
    {'template_name': 'registration/login.html'}, 'login'),
)
