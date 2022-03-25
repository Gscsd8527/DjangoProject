from django.shortcuts import render,HttpResponse,redirect
# 从utils文件夹下的code文件导入 check_code
from Utlis.code import check_code
from .models import UserInfo
from .forms import LoginForm
from django.views import View
from django import http
from django_redis import get_redis_connection
from Utlis.captcha.captcha import captcha


def code(request):
    """
    生成图片验证码
    """
    img, random_code = check_code()
    request.session['random_code'] = random_code
    from io import BytesIO
    # 实现了在内存中操作bytes
    stream = BytesIO()
    # 将二维码最终转为png格式
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def login(request):
    """
    用户登陆
    """
    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    code = request.POST.get('code')
    if code in [None, '']:
        return render(request, 'login.html', {'msg': '验证码没填'})
    if code.upper() != request.session['random_code'].upper():
        return render(request, 'login.html', {'msg': '验证码错误'})
    user = UserInfo.objects.filter(username=user, password=pwd)
    if user:
        return redirect('https://www.baidu.com')
    return render(request, 'login.html', {'msg': '用户名或密码错误'})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = UserInfo.objects.filter(username=username, password=password)
            if user:
                return redirect('https://www.baidu.com')
    else:
        form = LoginForm()
    # 跳转登录页面
    return render(request, 'user_login.html', context={'form':form})


class ImageCodeView(View):
    def get(self, request):
        # 生成图形验证码
        uuid = request.GET.get('uuid')
        print('UUID = ', uuid)
        text, image = captcha.generate_captcha()
        # 使用配置的redis数据库的别名，创建连接到redis的对象
        redis_conn = get_redis_connection('img_code')
        # redis_conn.setex('key', '过期时间', 'value')
        redis_conn.setex('img_%s' % uuid, 300, text)  # 有效时间是300秒
        # 响应图形验证码: image/jpg
        return http.HttpResponse(image, content_type='image/jpg')


def login_2(request):
    """
    用户登陆
    """
    if request.method == 'GET':
        return render(request,'login_2.html')
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    code = request.POST.get('code')
    uuid = request.POST.get('uuid', '9b4381ed-06da-4ff6-ab56-56fbcbec5ef2')  # 先写死
    print(f'code = {code}  uuid = {uuid}')
    redis_conn = get_redis_connection('img_code')
    uuid_code = redis_conn.get(f'img_{uuid}')
    uuid_code = str(uuid_code, 'utf-8')
    print(f'uuid_code = {uuid_code}')
    if uuid_code in [None, '']:
        return render(request, 'login_2.html', {'msg': '验证码没填'})
    if code.upper() != uuid_code.upper():
        return render(request, 'login.html',{'msg':'验证码错误'})
    user = UserInfo.objects.filter(username=user, password=pwd)
    if user:
        return redirect('https://www.baidu.com')
    return render(request, 'login_2.html', {'msg': '用户名或密码错误'})

