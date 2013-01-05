from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from catalog.models import Category, Product, ProductReview
from django.core import urlresolvers, serializers
from django.http import HttpResponseRedirect, HttpResponse
from catalog.forms import ProductAddToCartForm, ProductReviewForm
from cart import cart
from stats import stats
from ecomstore.settings import PRODUCTS_PER_ROW
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import simplejson



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
    product_reviews = ProductReview.approved.filter(product=product).order_by('-date')
    review_form = ProductReviewForm()
    return render_to_response("catalog/product.html", locals(),
        context_instance=RequestContext(request))


def get_json_products(request):
    products = Product.objects.all()
    products = products[0:1]
    json_products = serializers.serialize("json", products)
    return HttpResponse(json_products, content_type="application/javascript; charset=utf-8")

@login_required
def add_review(request):
    form = ProductReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        slug = request.POST.get('slug')
        product = Product.active.get(slug=slug)
        review.user = request.user
        review.product = product
        review.save()
        template = "catalog/product_review.html"
        html = render_to_string(template, {'review': review })
        response = simplejson.dumps({'success':'True', 'html': html})
    else:
        html = form.errors.as_ul()
        response = simplejson.dumps({'success':'False', 'html': html})
    return HttpResponse(response,content_type='application/javascript; charset=utf-8')
