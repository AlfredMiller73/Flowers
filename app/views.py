from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from order.models import OrderItem, Order
from django.contrib.auth.models import User
from django.db import models
from blog.models import Blog
from product.models import Product, Category
from cart.cart import Cart

def home(request):
    """Renders the home page."""
    cart = Cart(request)
    categories = Category.objects.order_by('name')
    products = Product.objects.order_by('-created')
    last = Blog.objects.order_by('-posted')[:3]
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Lotus',
            'cart': cart,
            'last': last,
            'categories': categories,
            'products': products,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'cart': cart,
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    cart = Cart(request)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
        	'cart': cart,
            'title':'Автосервис Локнянский район',
            'message':'Вас приветствует компания «СТО»!',
            'year':datetime.now().year,
        }
    )

def registration(request):
    """Renders the registration page."""
    cart = Cart(request)
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm(request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации

            reg_f.save() # сохраняем изменения после добавления данных

            return redirect('login') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
        'regform': regform, # передача формы в шаблон веб-страницы
        'cart': cart,
        'year':datetime.now().year,
        }
)

@login_required(login_url='/login/')
def userorders(request):
    cart = Cart(request)
    orders = Order.objects.filter(user = request.user)
    items = OrderItem.objects.filter(username = request.user)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/userorders.html',
        {
            'title':'Мои заказы',
            'cart': cart,
            'items': items,
            'orders': orders,
            'year':datetime.now().year,
        }
    )
