from django.urls import path
from order.views import OrderCreate, AdminOrderDetail
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.OrderCreate, name='OrderCreate'),
    path('admin/order/<order_id>/', views.AdminOrderDetail, name='AdminOrderDetail'),  
]

