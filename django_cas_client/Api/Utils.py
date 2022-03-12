import functools
from django.shortcuts import redirect, reverse

def LoginRequired(func):
    """
    自定义一个验证是否登录的装饰器
    :param func:
    :return:
    """
    @functools.wraps(func)
    def check_login(request):
        if not request.user.is_authenticated:
            next_url = request.path_info  # 获取当前路径
            print(f'当前路径 next_url = {next_url}')
            # return redirect('/login')
            # return redirect(reverse('cas_ng_login', kwargs={'next', next_url}))
            # return redirect('/login', next=next_url) # 无效
            return redirect(f'/login/?next={next_url}')  # 传参数传不过去，只好出此下策
        else:
            return func(request)
    return check_login
