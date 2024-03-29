"""django_cas_client URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import django_cas_ng.views as cas_views
"""
django_cas_ng 的版本为： django-cas-ng==4.1.1
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Api.urls", namespace="api")),  # 接入其它视图
    path('login/', cas_views.LoginView.as_view(), name='cas_ng_login'),  # cas服务的登陆视图
    path('logout/', cas_views.LogoutView.as_view(), name='cas_ng_logout'),  # cas服务的登出视图
]
