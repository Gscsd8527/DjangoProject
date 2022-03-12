from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import logout


def Index(request):
    if request.user.is_authenticated:
        print('已经登录了')
        print(dir(request.user))
        return HttpResponse(
            '<p>Welcome to <a href="https://djangocas.dev">django-cas-ng</a>.</p><p>You logged in as <strong>%s</strong>.</p><p><a href="/logout">Logout</a></p>' % request.user)
    else:
        print('未登录')
        return HttpResponse(
            '<p>Welcome to <a href="https://djangocas.dev">django-cas-ng</a>.</p><p><a href="/client/">Login</a></p>')


def MyIndex(request):
    if request.user.is_authenticated:
        username = request.user.username
        password = request.user.password
        cookies = request.COOKIES
        get_arg = request.GET.dict()
        post_arg = request.POST.dict()
        data_json = {
            'username': username,
            'password': password,
            'cookies': cookies,
            'get_arg': get_arg,
            'post_arg': post_arg,
        }
        return JsonResponse(data_json)
    else:
        return redirect(settings.LOGIN_URL)


@login_required
def testClientSSO(request):
    print(dir(request.user))
    username = request.user.username
    password = request.user.password
    cookies = request.COOKIES
    get_arg = request.GET.dict()
    post_arg = request.POST.dict()
    data_json = {
        'username': username,
        'password': password,
        'cookies': cookies,
        'get_arg': get_arg,
        'post_arg': post_arg,
    }
    return JsonResponse(data_json)


@login_required
def LogoutView(request):
    """
    登出操作
    看了一圈发现 django-simple-sso 好像没有自带的sso操作
    :param request:
    :return:
    """
    print('登出')
    logout(request=request)
    return redirect('/')
