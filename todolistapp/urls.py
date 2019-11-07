from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addtodo,name='add'),
    path('complete/<todo_id>', views.completed, name='complete'),
    path('delete', views.deleteAll, name='delete'),
    path('delcomp', views.deleteComplete, name='delcomp')
]