from django.db import models

# Create your models here.
# 这里可以不用生成迁移，因为在之前的项目中就已经生成了，现在想要使用之前表的数据的话，
# 只需要将之前设置好的表的model，复制过来即可，表名要和数据库中的一致，这样才能使用表，表数据在demo_test中已经定义过了
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField()
    bcommet = models.IntegerField()
    isDelete = models.BooleanField()
    class Meta():
        db_table = 'bookinfo'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField()
    book = models.ForeignKey('BookInfo', on_delete=True)
    class Meta():
        db_table = 'demo_test_heroinfo'

    # 在模板中测试这个函数
    def showname(self):
        return self.hname
