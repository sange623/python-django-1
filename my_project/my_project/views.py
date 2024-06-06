from django.shortcuts import render

def About(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def index(request):
    return render(request,"index.html")
def products(request):
    return render(request,"products.html")
def single_products(request):
    return render(request,"single-product.html")
