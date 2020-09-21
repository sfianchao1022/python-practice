from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


# Create your views here.
def index(request):  # 每個view function都要有request
    item = Products.objects.all()
    #  render函式中要加request 變數用dictionary包起來
    return render(request, 'index.html', {'fruits': item})  # 用item替換index.html中的變數fruits


def new(request):
    return HttpResponse('this is a new product')
