from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,reverse

# Create your views here.

def detail(request, p1):
    return HttpResponse('year: {}'.format(p1))

# 位置参数，p1 ,p2, p3的值是按照位置得到值的
def index(request, p1, p2, p3):
    return HttpResponse('year: {}, month: {}, day: {}'.format(p1, p2, p3))

# 展示链接的页面
def getTest1(request):
    return render(request, 'test1/getTest1.html')

# 接收一键一值的情况
def getTest2(request):
    # 根据键值接收值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    # 构造上下文
    context = {
        'a': a1,
        'b': b1,
        'c': c1
    }
    # 向模板中传递上下文，并调用模板进行渲染
    return render(request, 'test1/getTest2.html', context)

# 接收一键多值的情况
def getTest3(request):
    a1 = request.GET['a']
    a1 = request.GET.getlist('a')  # 假如a的值有多个，想要接收所有的值的话，使用getlist这个方法
    context = {
        'a': a1
    }
    return render(request, 'test1/getTest3.html', context)


def postTest1(request):
    return render(request, 'test1/postTest1.html')

def postTest2(request):
    uname = request.POST['uname']
    # 下面这种方式也可以得到值
    uname = request.POST.get('uname')
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    # uhobby = request.POST['uhobby']
    context = {
        'uname': uname,
        'upwd': upwd,
        'ugender': ugender,
        'uhobby': uhobby,
    }
    return render(request, 'test1/postTest2.html', context)


# cookie 练习
def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    # if cookie.has_key('t1'):
    # 只要cookie中带有t1,就将t1的值打印到页面上
    if cookie['t1']:
        response.write(cookie['t1'])

    # response.set_cookie('t1', 'abc')
    return response


def redTest1(request):
    # return HttpResponseRedirect('/test/redTest2/')
    # 也可使用下面的方法
    # return redirect('/test/redTest2/')
    # 也可使用下面的方法，省写路径，不过在url配置中要加name='redTest2'，test1表示app_name的名字，redTest2表示视图函数的别名
    return redirect(reverse('test1:redTest2'))

def redTest2(request):
    return HttpResponse("这是重定向来的页面")


# 通过用户登录练习session
def session1(request):
    # uname = request.session['myname']
    uname = request.session.get('myname', "未登录状态")
    context = {
        'uname': uname
    }
    return render(request, 'test1/session1.html', context)

def session2(request):
    return render(request, 'test1/session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    # 将用户名存入到session中
    request.session['myname'] = uname
    request.session.set_expiry(0)  # 关闭浏览器就过期
    return redirect('/test/session1/')

# 删除session
def session3(request):
    del request.session['myname']
    return redirect('/test/session1/')
