# from django.contrib import admin
#
# # Register your models here.
# from demo_test.models import *
#
# # 这个类的作用是： 在admin管理中显示出来的字段信息，想显示几个写几个
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcommet', 'isDelete']  # 显示的字段，先后顺序表示显示顺序
#     list_filter = ['btitle']  # 以哪个来过滤
#     search_fields = ['btitle']  # 以哪个字段来搜索，admin中就会出现一个搜索栏
#     list_per_page = 10  # 一页放多少条数据
#     #  在添加和修改页面可以将属性进行分组
#     fieldsets = [
#         ('base', {'fields': ['btitle']}),
#         ('super', {'fields': ['bpub_date']}),
#     ]
#
#
# class HeroInfoAdmin(admin.ModelAdmin):
#     list_display = ['hname']  # 显示的字段，先后顺序表示显示顺序
#
# # 不写BookInfoAdmin类的话，那么register中就不用写BookInfoAdmin这个值，写这个的意义是将这个值注册一下
# # 表示这个类起作用了
# admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(HeroInfo, HeroInfoAdmin)
