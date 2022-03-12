from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def MyLoginView(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        next = request.GET.get('next')
        print(f'next = {next}')
        return HttpResponse(next)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print('user= ', user)
        print('user= ', dir(user))
        return HttpResponse("登录成功")
