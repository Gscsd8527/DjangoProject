from django.shortcuts import render
from django.http import *
from .models import *
# Create your views here.

def index(request):
    # return HttpResponse('hello world')
    bookList = BookInfo.objects.all()
    context = {
        'list': bookList
    }
    return render(request, 'demo/index1.html', context)


def show(request, id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()  # 通过外键关联得到heroinfo表中对应的信息
    context = {
        'list': herolist
    }
    return render(request, 'demo/show.html', context)
