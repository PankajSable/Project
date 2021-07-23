from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product

# Create your views here.
def product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        weight = request.POST.get('weight')
        price = request.POST.get('price')
        createdat = request.POST.get('createdat')
        updatedat = request.POST.get('updatedat')
        product = Product(name=name,weight=weight,price=price,createdat=createdat,updatedat=updatedat)
        product.save()
    return render(request,'product.html')
    