from django.shortcuts import HttpResponse
from django.http.response import JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout, login
from .Utils import LoginRequired
# Create your views here.

def ShowView(request):
    if request.user.is_authenticated:
        resp = {
            'code': 200,
            'msg': '登录成功',
            'data': f'登录的用户名为 {request.user.username}',
        }
        # login(request, request.user)

        # 配置了多个身份验证后端，因此必须提供`backend`参数或在用户上设置`backend`属性
        login(request, request.user, backend="django.contrib.auth.backends.ModelBackend")
        return JsonResponse(resp)
    else:
        return HttpResponseRedirect('/login')

@LoginRequired
def MyShowView(request):
    """
    通过装饰器来判断是否登录
    :param request:
    :return:
    """
    return HttpResponse("查看数据")


def Index(request):
    # 判断是否登录的
    if request.user.is_authenticated:
        return HttpResponse(
            '<p>Welcome to <a href="https://djangocas.dev">django-cas-ng</a>.</p><p>You logged in as <strong>%s</strong>.</p><p><a href="/logout">Logout</a></p>' % request.user)
    else:
        return HttpResponse(
            '<p>Welcome to <a href="https://djangocas.dev">django-cas-ng</a>.</p><p><a href="/login">Login</a></p>')
