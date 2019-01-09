from django.shortcuts import render, HttpResponse
from django.conf import settings
import os
from test3.models import *
from django.core.paginator import *
# Create your views here.

def index(request):
    return render(request, 'test3/index.html')


# 测试中间件，在项目下新建一个MyException文件，在里面定义类，继承MiddlewareMixin，
# 然后在setting的MIDDLEWARE中将异常类导入即可。
# 也可以新建一个文件专门来存放中间件文件
def MyExp(request):
    a1 = int('abc')
    return HttpResponse('Hello')


# 文件上传并存储到相应的目录
def uploadPic(request):
    return render(request, 'test3/upload.html')

def uploadHandle(request):
    pic1 = request.FILES['pic1']
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    with open(picName, 'wb+') as pic:
        for c in pic1.chunks():
            pic.write(c)
    # return HttpResponse(picName)
    return HttpResponse('<img src="/static/media/%s"/>' % pic1.name)


# 进行分页练习
def herolist(request, pindex):
    print('pindex=', pindex)
    if pindex == '':
        pindex = '1'
    list = UserInfo.objects.all()
    pagenator = Paginator(list, 5)
    page = pagenator.page(int(pindex))
    context = {'page': page}
    return render(request, 'test3/herolist.html', context)
