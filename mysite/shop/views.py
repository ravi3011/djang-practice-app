from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/index.html')


def about(request):
    return HttpResponse("i about page")

def contact(request):
    return HttpResponse("i am contact page")

def tracker(request):
    return HttpResponse("i amtracker page")

def search(request):
    return HttpResponse("i am search page")

def productView(request):
    return HttpResponse("i am product view")

def checkout(request):
    return HttpResponse("i am checkout")