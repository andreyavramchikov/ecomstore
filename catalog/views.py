from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from catalog.models import Category, Product
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from catalog.forms import ProductAddToCartForm
from cart import cart
from stats import stats
from ecomstore.settings import PRODUCTS_PER_ROW



""" BEGINING WORK WITH GITHUB NOW"""

def index(request,template_name="catalog/index.html"):
    search_recs = stats.recommended_from_search(request)
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)

    page_title = "Musical Instruments and Sheet Musican for Musicans"
    return render_to_response(template_name,locals(),context_instance=RequestContext(request))

def show_category(request,category_slug, template_name="catalog/category.html"):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product_set.all()
    page_title = category.name
#    meta_keywords = c.meta_keywords
#    meta_description = c.meta_description
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))
   
   
def show_product(request, product_slug, template_name="catalog/product.html"):
    product = get_object_or_404(Product, slug=product_slug)
    categories = product.categories.all()
    page_title = product.name
    stats.log_product_view(request, product)

    meta_keywords = product.meta_keywords
    meta_description = product.meta_description
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
   
        if form.is_valid():
            cart.add_to_cart(request)
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(url)
    else:
        form = ProductAddToCartForm(request=request, label_suffix=':')
        
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    request.session.set_test_cookie()
    return render_to_response("catalog/product.html", locals(),
        context_instance=RequestContext(request))


   