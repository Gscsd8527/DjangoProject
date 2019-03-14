from django.contrib import admin
from test4.models import StudentModel
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'age']


admin.site.register(StudentModel, StudentAdmin)
