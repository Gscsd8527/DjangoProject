from django.shortcuts import render, HttpResponse
from test2.models import *
# Create your views here.
def index(request):
    # hero = HeroInfo.objects.get(pk=1)
    # context = {'hero': hero}

    list = HeroInfo.objects.all()
    print('list= ', list)
    context = {
        'list': list
    }
    return render(request, 'test2/index.html', context)

# 反向解析，反向解析在test2/index.html页面中，涉及namespace和name
def show(request, id):
    context = {
        'id': id
    }
    return render(request, 'test2/show.html', context)


# 用于练习模板的继承,base.html是主html，index2继承于index2.html
def index2(request):
    return render(request, 'test2/index2.html')

def user1(request):
    context = {
        'name': '习大大'
    }
    return render(request, 'test2/user1.html', context)

def user2(request):
    return render(request, 'test2/user2.html')

# html 转义
def htmlTest(request):
    context = {'t1': '<h1>123<h1>'}
    return render(request, 'test2/htmlTest.html', context)


# csrf
def csrf1(request):
    return render(request, 'test2/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)


# 验证码
def verifyCode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 创建背景色
    bgColor = (random.randrange(50, 100), random.randrange(50, 100), 0)
    # 规定宽高
    width = 100
    height = 25
    # 创建画布
    image = Image.new('RGB', (width, height), bgColor)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    text = 'ABCD'
    draw.text((0, 0), text)
    return HttpResponse()
