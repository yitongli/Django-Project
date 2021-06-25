from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def january(request):
    return HttpResponse("not eat meat")

def february(request):
    return HttpResponse("walk 20 minutes everyday")

