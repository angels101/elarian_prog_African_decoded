from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name= 'product'

urlpatterns = [
    path('', views.productlist, name='product_list'),
    #path('<int:id>', views.productdetail, name='product_detail'),
    path('<slug:product_slug>', views.productdetail, name='product_detail'),
]
