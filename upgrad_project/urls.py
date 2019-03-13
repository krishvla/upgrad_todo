"""upgrad_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from upgrad.views import index, alogin , logout_view, delete_list, update_list
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', alogin, name="alogin"),
    url(r'^index$', index, name="index"),
    url(r'^logout_view$', logout_view, name="logout"),
    url(r'^delete_list/(?P<pk>\d+)/$', delete_list, name='delete_list'),
    url(r'^update_list/(?P<pk>\d+)/$', update_list, name='update_list'),
]
