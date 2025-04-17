from django.urls import path

from .views import catalog, product

app_name = 'goods'  # при подключении namespace

urlpatterns = [
    path('', catalog, name='catalog'),
    path('product/', product, name='product'),
]
