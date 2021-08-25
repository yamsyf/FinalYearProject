from re import I
from django.http import HttpResponse
from django.shortcuts import render


 
def hello(request):
    return HttpResponse("Hello world ! ")

def homepage(request):

    return render(request, 'base.html', context=None)




