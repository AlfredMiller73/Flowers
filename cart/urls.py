from . import views
from django.urls import path
from django.conf.urls.static import static

app_name = 'cart'

urlpatterns = [
    path('', views.CartDetail, name='CartDetail'),
    path('remove/(<product_id>)/', views.CartRemove, name='CartRemove'),
    path('add/(<product_id>)/', views.CartAdd, name='CartAdd'),
]


