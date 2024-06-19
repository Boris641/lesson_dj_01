from django.shortcuts import render
from django.http import HttpResponse

def data(request):
    return HttpResponse("<h1>Впервые на Django</h1>")
def test(requ8est):
    return HttpResponse("<h1>Возвращайтесь на Django</h1>")

# Create your views here.
