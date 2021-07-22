from io import StringIO
import re
from django.shortcuts import render
from django.views.decorators import csrf
import mongoengine
from mongoengine.connection import connect
from mongoengine.queryset.queryset import QuerySet
from .docs import Doc2
from .docs import Doc3,Doc4
from itertools import chain
from django.db.models import Q
import operator
 
# 接收POST请求数据
def search_post(request):
    ctx ={}
    
    list1 = []
    checklist = ["12C2","C2H2__12C2-1H2"]
    molelist = request.POST.getlist("check")
    ctx['molelist'] = request.POST.getlist("check")
    if "12C2" in request.POST.getlist("check"):
        list1.append(51)
    if "C2H2__12C2-1H2" in request.POST.getlist("check"):
        list1.append(26)
    if request.POST:
        number = float(request.POST['q'])
        number1 = float(request.POST['p'])
        method = request.POST.get('method',None)
        

        print(type(Doc4.objects))
        
        final = Doc4.objects.order_by("v").filter(v__gt = number).filter(v__lt=number1).filter(M__exact=list1[0])
      
        
        #test = test.filter(Q(M__exact=))
        if len(list1) >1:
            for i in list1[1:]:
                final = chain(final,Doc4.objects.filter(v__gt = number).filter(v__lt=number1).filter(M__exact=i).order_by("v"))

        temp = list(final)
        print(temp[0].v)
        cmpfun = operator.attrgetter("v")
        temp.sort(key=cmpfun)
        wavelength = []
        frequency =[]
        Ierr_mic=[]
        E_f_mic=[]
        Ierr_GHz=[]
        E_f_GHz=[]
        for i in temp:
            # print(i.v)
            tempvalue = i.v/10000
            tempvalue1 = i.v*29.9792458
            # print(tempvalue)
            Ierr_mic.append(i.Ierr/10000)
            Ierr_GHz.append(i.Ierr*29.9792458)
            E_f_GHz.append(i.Ierr*29.9792458)
            E_f_mic.append(i.Ierr/10000)
            wavelength.append(tempvalue)
            frequency.append(tempvalue1)
        finallist = []
        Mole_list=[]
        for item in temp:

            if item.M == 51:
                Mole_list.append("C2")
            if item.M == 26:
                Mole_list.append("C2H2")
        counter =0
        for i in temp:

            tempdict = {
                'v': i.v,
                'M': i.M,
                'I': i.I,
                'A': i.A,
                'E_f' :i.E_f,
                'V_i' : i.V_i,
                'S':i.S,
                'V_f':i.V_f,
                'Q_i':i.Q_i,
                'Q_f':i.Q_f,
                'Ierr':i.Ierr,
                'g_i':i.g_i,
                'g_f':i.g_f,
                'q' : i.q,
                'wavelength':wavelength[counter],
                'frequency' :frequency[counter],
                'Ierr_GHz':Ierr_GHz[counter],
                'E_f_GHz':E_f_GHz[counter],
                'Ierr_mic':Ierr_mic[counter],
                'E_f_mic':E_f_mic[counter],
                'Mole':Mole_list[counter]
                }
            counter =counter+1
            finallist.append(tempdict)
          #  print(tempdict['S'])
        ctx['dic'] = finallist
        ctx['rlt'] = temp
        ctx['len'] = len(temp)
        
        ctx['wavelength'] = tempvalue
        str1 = '{:e}'.format(temp[0].v)
        print (type(temp[0].S))
        #print(listtemp)
        ctx['range'] = range(0,len(temp)-1)
        print(ctx['range'])
        ctx['Mole_list'] = []
        ctx['Method'] = method
        

            
        context={
            'length':len(temp),
        }
    return render(request, "newpost.html", context=ctx)

def search_post2(request):
    ctx ={}
    ctx1 = {}
    if request.POST:
        number = float(request.POST['q'])
        number1 = float(request.POST['p'])
        temp=Doc3.objects.filter(v__gt = number).filter(v__lt=number1).order_by("v")
        db_get_data = Doc3.objects.all()
        
        #temp[0].message
        listtemp = list(temp)
        #print("Ssasdasd")
        ctx['rlt'] = temp
        ctx['len'] = len(temp)
        ctx['list'] = listtemp
        ctx['range'] = range(0,1)
        print(ctx['range'])
        str1 = '{:e}'.format(temp[0].v)
        
        #print(listtemp)
        context={
            'length':len(temp),
        }
    return render(request, "post.html", context=ctx)

def isopo(request):
    ctx={}
    # if request.POST:
    #     ctx['rlt'] = request.POST['check'][]
    ctx['rlt'] = []
    
    if "C2" in request.POST.getlist("check"):
        ctx['rlt'].append("12C2")
    if "C2H2" in request.POST.getlist("check"):
        ctx['rlt'].append("C2H2__12C2-1H2")
    return render(request,"iso.html",ctx)

def userinput(request):
    ctx={}
    ctx['molelist']=[]
    if "12C2" in request.POST.getlist("check"):
        ctx['molelist'].append("12C2")
        print("try")
    if "C2H2__12C2-1H2" in request.POST.getlist("check"):
        ctx['molelist'].append("C2H2__12C2-1H2")
    return render(request,"newpost.html",ctx)
