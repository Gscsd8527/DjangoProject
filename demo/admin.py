from django.contrib import admin

# Register your models here.
from demo.models import *

# 关联对象注册 作用：在关联对象进行添加的时候的快捷方式
# 这个的作用是在于在关联上了BookInfoAdmin这个类，在admin页面中BookInfoAdmin增加、修改数据的页面上，也会显示HeroInfo这个表，相应的显示增加数据
# extra表示要增加几个HeroInfo这个表的数据
# 列： 在增加BookInfo这个表的页面上，会出现BookInfo这个表的字段信息和HeroInfo表的字段信息，extra为多少就有多少个HeroInfo表信息，增加BookInfo的同时能增加extra个HeroInfo

# class HeroInfoInline(admin.StackedInline): StackedInline表示默认形式，TabularInline是以表格的形式显示
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo  # 指定需要把哪个模型类嵌入进去
    extra = 3  # 而外嵌入几个


# 这个类的作用是： 在admin管理中显示出来的字段信息，想显示几个写几个
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']  # 显示的字段，先后顺序表示显示顺序
    list_filter = ['btitle']  # 以哪个来过滤
    search_fields = ['btitle']  # 以哪个字段来搜索，admin中就会出现一个搜索栏
    list_per_page = 10  # 一页放多少条数据
    #  在添加和修改页面可以将属性进行分组
    fieldsets = [
        ('base', {'fields': ['btitle']}),
        ('super', {'fields': ['bpub_date']}),
    ]

    inlines = [HeroInfoInline]  # 这句是和上面HeroInfoInline这个类是对应的，表示将这个类添加进去，如果和多个类关联的话就在列表中加


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname']  # 显示的字段，先后顺序表示显示顺序

# 不写BookInfoAdmin类的话，那么register中就不用写BookInfoAdmin这个值，写这个的意义是将这个值注册一下
# 表示这个类起作用了
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
