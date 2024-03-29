
from django import template
from cart import cart
from catalog.models import Category

register = template.Library()

@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return {'cart_item_count' : cart_item_count}


@register.inclusion_tag("tags/category_list.html")
def category_list(request_path):
    active_categories = Category.active.all()
    return {
            'active_categories' : active_categories,
            'request_path' : request_path
    }
    
from django.contrib.flatpages.models import FlatPage
@register.inclusion_tag("tags/footer.html")
def footer_links():
    flatpage_list = FlatPage.objects.all()
    return {'flatpage_list': flatpage_list }

@register.inclusion_tag("tags/product_list.html")
def product_list(products, header_text):
    return { 'products': products, 'header_text': header_text }
