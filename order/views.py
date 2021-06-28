from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string


@staff_member_required
def AdminOrderDetail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/detail.html', {'order': order})

#def OrderCreated(request):
#    return render(request, 'order/created.html')

def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(username = request.user, order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            #return HttpResponseRedirect('/order/created/')
            return redirect(reverse('home'))

    form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart,
                                                        'form': form})
