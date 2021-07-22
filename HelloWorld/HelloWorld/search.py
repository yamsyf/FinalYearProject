from django.http import HttpResponse
from django.shortcuts import render
# 表单
def search_form(request):
    return render(request, 'search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'qpp' in request.GET and request.GET['qpp']:
        message = '你搜索的内容为: ' + request.GET['qpp']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)