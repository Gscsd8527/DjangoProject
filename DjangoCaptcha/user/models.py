from django.db import models

# Create your models here.

class UserInfo(models.Model):
    """
    用户：划分角色
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True, verbose_name="用户名")  # 用户名设置成唯一值
    password = models.CharField(max_length=64, verbose_name="密码")
    real_name = models.CharField(max_length=50, verbose_name=u"真实姓名", default="")
    email = models.EmailField(max_length=254, unique=True, verbose_name="邮箱")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
