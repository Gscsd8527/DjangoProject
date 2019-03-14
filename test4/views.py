from django.shortcuts import render
from .models import StudentModel
from django.core.paginator import Paginator
# Create your views here.

def test(request):
    return render(request, 'test4/test.html')


def fenye(request, pageid):
    allList = StudentModel.objects.all()
    paginator = Paginator(allList, 6)
    page = paginator.page(pageid)
    return render(request, 'test4/page.html', {'students': page})

def ajaxstudents(request):
    return render(request, 'test4/ajaxstudents.html')

from django.http import JsonResponse
def studentsinfo(request):
    stus = StudentModel.objects.all()
    data = []
    for stu in stus:
        data.append([stu.name, stu.sex, stu.age])
    return JsonResponse({'data': data})


import time
def celery(request):
    print("hello, 这是celery耗时操作")
    time.sleep(5)
    print("hello, 这是celery耗时操作")
    return render(request, 'test4/celery.html')