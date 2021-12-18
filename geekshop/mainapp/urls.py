from django.urls import path, re_path
from mainapp import views as mainapp
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),
    re_path(r'^category/(?P<pk>\d+)/$', cache_page(3600)(mainapp.products)),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
