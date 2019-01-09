from django.contrib import admin

# Register your models here.
from test3.models import *

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'uname', 'upwd', 'isDelete']


admin.site.register(UserInfo, UserInfoAdmin)
