from django.db import models

# Create your models here.

# 自定义管理器
class BookInfoManager(models.Manager):
    def get_queryset(self):
        # 重写get_queryset方法，只要执行查询，就会调用这个方法
        # super(BookInfoManager, self).get_queryset()表示执行查询，filter(isDelete=False)表示在查询的基础上做个筛选
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    # 快捷对象创建方式二（官方推荐这种方法）
    # 管理器中也可写这个方法，现在不是类方法了，作用是相同的
    # 使用：
    #   from demo_test.models import BookInfo
    #   from datetime import datetime
    #   b = BookInfo.books2.create('abc', datetime(1990, 1, 1))
    #   b.save()
    #   数据库中会插入这条数据
    def create(self, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.ImageField(default=0)
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    # 元选项
    class Meta:
        db_table = 'bookinfo'  # 指定表的名字，如果不指定的话，默认的是demo_test_bookinfo(<app_name>_<model_name>)

    # 表明BookInfo有两个管理器
    books1 = models.Manager()  # 这个是默认会调用的，写这个的目的是和后面那个区分开来
    books2 = BookInfoManager()  # 自定义管理器，在查询的时候做了一些过滤
    # 使用
    # 》》》from demo_test.models import BookInfo
    # 》》》BookInfo.books1.all() 得到所有数据
    # 》》》BookInfo.books2.all() 得到isDelete为0的数据

    # 快捷对象创建方式一
    # 自定义一个模型类方法，写成类方法，自动创建类对象，好处是每次创建对象都不用去写这些值
    # 坏处： 模型类中的一些方法不能用了，因为被覆盖了，原因是models.Model已经用了init做了很多的方法，列如：b = BookInfo.object.all()就不能用了
    # 使用：
    #   from demo_test.models import BookInfo
    #   from datetime import datetime
    #   b = BookInfo.create('abc', datetime(1990, 1, 1))
    #   b.save()
    #   数据库中会插入这条数据
    @classmethod
    def create(cls, btitle, bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=True)


