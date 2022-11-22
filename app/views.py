from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def venky(request):
    return HttpResponse('venky mass')
