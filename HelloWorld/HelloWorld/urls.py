"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from . import views,search,search2
from .views import Docs

urlpatterns = [
    #path('admin/', admin.site.urls),
    url('hello/',views.hello),
    url('runoob/', views.runoob,name='runoob'),
    url(r'^hello/$', views.runoob),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post,name="C2"),
    url(r'^search-post1/$', search2.search_post2,name="C2H2"),
    url('db',Docs.as_view(),name = 'student'),
    url('newpost/', views.testnoob,name='newpost'),
    url('post/', views.runoob1,name='post'),
    url('post1/',search2.isopo,name='post1'),
    url('post2/',search2.userinput,name='post2')
    
]
