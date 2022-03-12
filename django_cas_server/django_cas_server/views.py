from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(username, password, email)
        User.objects.create_user(username=username, password=password, email=email)
        return HttpResponse("创建用户成功")
    else:
        return HttpResponse("GET 请求")


