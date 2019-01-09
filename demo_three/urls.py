"""demo_three URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('demo/', include('demo.urls', namespace='demo')),
    url('^', include('demo.urls', namespace='demo')),
    path('demotest/', include('demo_test.urls', namespace='demo_test')),
    path('test/', include('test1.urls', namespace='test')),
    path('test2/', include('test2.urls', namespace='test2')),
    path('test3/', include('test3.urls', namespace='test3')),
]
