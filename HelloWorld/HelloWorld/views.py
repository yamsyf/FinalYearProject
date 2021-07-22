from re import I
from django.http import HttpResponse
from django.shortcuts import render


 
def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    context = {}
    context['hellos'] = 'Hello World!'
    views_name = 'sss'
    views_list = ['1','2','3']
    num = 1
    return render(request, 'base.html', {"views_listsss":views_list,"number":num})
def runoob1(request):
    context = {}
    context['hellos'] = 'Hello World!'
    views_name = 'sss'
    views_list = ['1','2','3']
    num = 1
    return render(request, 'iso1.html', {"views_listsss":views_list,"number":num})

def testnoob(request):

    return render(request, 'iso.html',context=None)

from .docs import Doc
from django.views.generic import View

class Docs(View):
    def get(self,request):
        
        result = Doc.objects.filter(pid=374229)
        print(result[0].qid)
        print(result[0].relevancy)
        
        return render(request,'search_form.html',{"passage":result[0].passage,"qid":result[0].qid})