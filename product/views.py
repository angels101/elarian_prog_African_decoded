from django.shortcuts import render
from .models import Product
# Create your views here.
def productlist(request):
    productlist = Product.objects.all()
    #print(productlist)
    context ={'product_list' : productlist}
    template ='Product/product_list.html'
    return render(request, template, context)

def productdetail(request, product_slug):
    print(product_slug)
    productdetail = Product.objects.get(slug=product_slug)
    template ='Product/product_detail.html'
    context ={'product_detail' : productdetail}
    return render(request, template, context)