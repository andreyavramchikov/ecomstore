from django.conf.urls import patterns, include, url

urlpatterns = patterns('cart.views',
    (r'^cart/$', 'show_cart', { 'template_name': 'cart/cart.html' }, 'show_cart'),
)