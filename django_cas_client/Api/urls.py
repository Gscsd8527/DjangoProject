from django.urls import path
from .views import Index, ShowView, MyShowView

app_name = 'api'

urlpatterns = [
    path('', Index, name='index'),
    path('show/', ShowView, name='show'),
    path('myshow/', MyShowView, name='myshow'),
]
