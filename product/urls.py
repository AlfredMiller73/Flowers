from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from product import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductList, name='ProductList'),
    path('<category_slug>/', views.ProductList, name='ProductListByCategory'),
    path('<slug>', views.ProductDetail, name='ProductDetail'),
]

