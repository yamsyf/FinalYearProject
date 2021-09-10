"""ExoMol URL Configuration

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
from . import views,search

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    #path('admin/', admin.site.urls),
    url('hello/',views.hello),
    url('searchpage/', views.homepage,name='page1'),
    url(r'^search-post/$', search.search_post,name="C2"),
    url('post1/',search.isopo,name='post1'),
    url('post2/',search.userinput,name='post2'),
    url(r'^stark/crm/Download/', search.file_down,name='crm_download'),
    url(r'^stark1/crm/Download/', search.file_down1,name='crm_download1000'),
    url('homepage/',search.homepage,name= 'home')
    
]
urlpatterns += staticfiles_urlpatterns()