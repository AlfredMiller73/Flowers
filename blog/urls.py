from django.urls import path  
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
  
app_name = 'blog'  
  
urlpatterns = [  
    path('', views.blog, name='blog'),
    path('<id>/', views.blogpost, name='blogpost'),
]

