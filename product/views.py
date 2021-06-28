from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from product.models import Category, Product, Review
from product.forms import ReviewProduct
from cart.forms import CartAddProductForm
from cart.cart import Cart
from datetime import datetime
from django.http import HttpRequest
from django.template import RequestContext


# Страница с товарами
def ProductList(request, category_slug=None):
    cart = Cart(request)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html', {
    	'title': 'Все товары',
    	'cart': cart,
        'category': category,
        'categories': categories,
        'products': products,
        'year':datetime.now().year,
    })

# Страница товара
def ProductDetail(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug, available=True)
    reviews = Review.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    if request.method == "POST": 
       form = ReviewProduct(request.POST)
       if form.is_valid():
           comment_f = form.save(commit=False)
           comment_f.author = request.user 
           comment_f.date = datetime.now() 
           comment_f.product = Product.objects.get(slug=slug) 
           comment_f.save() 
           return redirect('product:ProductList', slug=slug) 
    else:
        form = ReviewProduct() 
    return render(request, 'product/detail.html',
                             {
                             	'title': 'Товар',
                             	'cart': cart,
                             	'product': product,
                                'reviews': reviews,
                                'cart_product_form': cart_product_form,
                                'year':datetime.now().year,
                             }
                  )
