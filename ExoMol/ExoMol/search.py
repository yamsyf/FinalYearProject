from io import StringIO
import re
from django.shortcuts import render
from django.views.decorators import csrf
import mongoengine
from mongoengine.connection import connect
from mongoengine.queryset.queryset import QuerySet
from .docs import Doc4
from itertools import chain
from django.db.models import Q
import operator
import json
import codecs
import csv
 
# 接收POST请求数据
def search_post(request):
    ctx ={}
    
    list1 = []
    checklist = ["12C2","C2H2__12C2-1H2"]
    molelist = request.POST.getlist("check")
    ctx['molelist'] = request.POST.getlist("check")
    ctx['filter'] = request.POST.getlist("filter")
    
    Doc4.create_index([("v", 1)])
    
    if "12C2" in request.POST.getlist("check"):
        list1.append(51)
    if "C2H2__12C2-1H2" in request.POST.getlist("check"):
        list1.append(26)
    if "AI1H" in request.POST.getlist("check"):
        list1.append(50)
    if "14N-1H3" in request.POST.getlist("check"):
        list1.append(11)
    if "1H3-16O" in request.POST.getlist("check"):
        list1.append(52)
    if "1H2-16O" in request.POST.getlist("check"):
        list1.append(1)
    if "12C-16O2" in request.POST.getlist("check"):
        list1.append(2)
    if request.POST:
        number = float(request.POST['q'])
        number1 = float(request.POST['p'])
        method = request.POST.get('method',None)
        
        print(method)
        if method=="frequency":
            number= number/29.9792458
            number1=number1/29.9792458
        if method=="wavelength":
            number = number*10000
            number1 = number1*10000
        if "cutting" in request.POST.getlist("filter"):
            final = Doc4.objects.order_by("v").filter(v__gt = number).filter(v__lt=number1).filter(M__exact=list1[0]).filter(S__gt = 1e-40)
      
        
        #test = test.filter(Q(M__exact=))
            if len(list1) >1:
                for i in list1[1:]:
                    final = chain(final,Doc4.objects.filter(v__gt = number).filter(v__lt=number1).filter(S__gt = 1e-40).filter(M__exact=i).order_by("v"))
        else:
            final = Doc4.objects.order_by("v").filter(v__gt = number).filter(v__lt=number1).filter(M__exact=list1[0])
            if len(list1) >1:
                for i in list1[1:]:
                    final = chain(final,Doc4.objects.filter(v__gt = number).filter(v__lt=number1).filter(M__exact=i).order_by("v"))
 
       
        temp = list(final)

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
        Reference_list = []
        for item in temp:

            if item.M == 51:
                Mole_list.append("C2")
                Reference_list.append("10.1093/mnras/staa229")
            if item.M == 26:
                Mole_list.append("C2H2")
                Reference_list.append("10.1093/mnras/sty1542 , 10.1093/mnras/sty2050")
            if item.M ==50:
                Mole_list.append("ALH")
                Reference_list.append("10.1093/mnras/sty1542")
            if item.M ==11:
                Mole_list.append("NH3")
                Reference_list.append("10.1093/mnras/stz2778")
            if item.M ==52:
                Mole_list.append("H3O")
                Reference_list.append("10.1051/0004-6361/202038350")
            if item.M ==1:
                Mole_list.append("H2O")
                Reference_list.append("10.1093/mnras/sty1877")
            if item.M ==2:
                Mole_list.append("CO2")
                Reference_list.append("10.1093/mnras/staa1874")
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
                'Mole':Mole_list[counter],
                'reference':Reference_list[counter]
                }
            counter =counter+1
            finallist.append(tempdict)
        
           
        with codecs.open('./static/data.csv','w','utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["M","I","v","S","A","E_f","V_i","V_f","Q_i","Q_f","Ierr","g_i","g_f","DOI"])
            for data in finallist:
                writer.writerows([[data["M"],data["I"],data["v"],data["S"],data["A"],data["E_f"],data["V_i"],data["V_f"],data["Q_i"],data["Q_f"],data["Ierr"],data["g_i"],data["g_f"],data["reference"]]])
        if len(finallist)>1000:
            with codecs.open('./static/data1000.csv','w','utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["M","I","v","S","A","E_f","V_i","V_f","Q_i","Q_f","Ierr","g_i","g_f","DOI"])
                for data in finallist[:1000]:
                    writer.writerows([[data["M"],data["I"],data["v"],data["S"],data["A"],data["E_f"],data["V_i"],data["V_f"],data["Q_i"],data["Q_f"],data["Ierr"],data["g_i"],data["g_f"],data["reference"]]])

        ctx['dic'] = finallist
        
        ctx['len'] = len(finallist)
        ctx['number'] = ["1","2","3"]
        
        
   
        #print(listtemp)
      

        
        ctx['Method'] = method
        

            
        context={
            'length':len(temp),
        }
    return render(request, "searchpage.html", context=ctx)



def isopo(request):
    ctx={}
    # if request.POST:
    #     ctx['rlt'] = request.POST['check'][]
    ctx['rlt'] = []
    
    if "C2" in request.POST.getlist("check"):
        ctx['rlt'].append("(12C2)")
    if "C2H2" in request.POST.getlist("check"):
        ctx['rlt'].append("C2H2__12C2-1H2")
    if "aih" in request.POST.getlist("check"):
        ctx['rlt'].append("aih")
    if "NH3" in request.POST.getlist("check"):
        ctx['rlt'].append("NH3")
    if "H3O" in request.POST.getlist("check"):
        ctx['rlt'].append("H3O")
    if "H2O" in request.POST.getlist("check"):
        ctx['rlt'].append("H2O")
    if "CO2" in request.POST.getlist("check"):
        ctx['rlt'].append("CO2")
    print(ctx)

    
    return render(request,"iso.html",{
        'rlt':json.dumps(ctx['rlt'])
        })

def userinput(request):
    ctx={}
    ctx['molelist']=[]
    if "12C2" in request.POST.getlist("check"):
        ctx['molelist'].append("12C2")
        
    if "C2H2__12C2-1H2" in request.POST.getlist("check"):
        ctx['molelist'].append("C2H2__12C2-1H2")
    if "AI1H" in request.POST.getlist("check"):
        ctx['molelist'].append("AI1H")
    if "14N-1H3" in request.POST.getlist("check"):
        ctx['molelist'].append("14N-1H3")
    if "1H3-16O" in request.POST.getlist("check"):
        ctx['molelist'].append("1H3-16O")
    if "1H2-16O" in request.POST.getlist("check"):
        ctx['molelist'].append("1H2-16O")
    if "12C-16O2" in request.POST.getlist("check"):
        ctx['molelist'].append("12C-16O2")    
    
  
    return render(request,"searchpage.html",ctx)

from django.http import FileResponse
def file_down(request):  
    file=open('./static/data.csv','rb')  
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="data.csv"'  
    return response 
def file_down1(request):  
    file=open('./static/data1000.csv','rb')  
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="data1000.csv"'  
    return response 