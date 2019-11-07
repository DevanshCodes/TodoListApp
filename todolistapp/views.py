from django.shortcuts import render
from .models import Todo
# Create your views here.

def index(request):
    todo_list = Todo.objects.order_by('id')
    context= {'todo' : todo_list}

    return render(request,'todolistapp/index.html',context)
