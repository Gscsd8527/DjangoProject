from django.urls import path
from user import views

app_name = 'users'

urlpatterns = [
    # 第一种图片验证码方式: 自己使用PIL去制作验证码,并将验证码存在session中，在登录的时候进行校验
    path('login/', views.login, name='login'),


    # 第二种图片验证码方式: 用Django的 django-simple-captcha，再加上一个forms表单，
    # 将验证码存入mysql数据库中，app中导入captcha
    path('login_1/', views.user_login, name='login_1'),


    # 第三种图片验证码方式: 导入外部的一个包，用于生成图片验证码，存入redis中，
    # 由前端生成一个uuid码，用于标记二维码图片，前端传入的验证码和uuid，再拿到验证码跟从redis中取出来的uuid的值做对比
    # 用redis做缓存
    path('image_codes/', views.ImageCodeView.as_view()),
    path('login_2/', views.login_2,  name='login_2'),
]
