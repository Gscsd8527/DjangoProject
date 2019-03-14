from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=30, verbose_name="名字")
    sex = models.CharField(max_length=10, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    datatime = models.DateTimeField(auto_now=True, verbose_name="时间")
    class Meta:
        db_table = 'student'

