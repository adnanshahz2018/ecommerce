from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def hello(request):
#     return HttpResponse('<h1>Hello World<h1>')


# Create your views here.

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def main(request):
    context = {}
    return render(request, 'store/main.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


# ...    