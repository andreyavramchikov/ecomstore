from django.conf.urls import patterns, include, url

urlpatterns = patterns('catalog.views',
   (r'^$', 'index', { 'template_name':'catalog/index.html'}, 'catalog_home'),
   (r'^category/(?P<category_slug>[-\w]+)/$','show_category', {'template_name':'catalog/category.html'}, 'catalog_category'),
   (r'^product/(?P<product_slug>[-\w]+)/$','show_product'),
)
