from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    store = Product.objects.all()
    return render(request, 'index.html',
                  {'products': store})
