from django.shortcuts import render
from demo_test.models import *
from django.db.models import Max, F, Q
# Create your views here.
def index(request):
    list = BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    # 聚合函数
    max_date = BookInfo.books1.aggregate(Max('bpub_date'))  # 最大值
    list = BookInfo.books1.filter(bread__gt=F("bcommet"))  # 阅读量大于评论量

    # 下面这两条语句相等，是逻辑与，表示两个条件都符合
    # list = BookInfo.books1.filter(pk__lt=6, btitle__contains="1")  # 查询id小于6，并且名字当中包含1的
    # list = BookInfo.books1.filter(pk__lt=6).filter(btitle__contains="1")  # 查询id小于6，并且名字当中包含1的
    # 逻辑或，表示两个条件符合一个就可以，想实现逻辑或，就必须使用Q对象
    # list = BookInfo.books1.filter(Q(pk__lt=4) | Q(btitle__contains='1'))
    context = {
        'list': list,
        'max_date': max_date
    }
    print(context)
    return render(request, 'demo_test/index.html', context)

