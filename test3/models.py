from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=40)
    isDelete = models.BooleanField()

