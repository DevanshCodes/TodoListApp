from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def index(request):
    form = TodoForm()
    todo_list = Todo.objects.order_by('id')
    context= {'todo' : todo_list, 'form':form}

    return render(request,'todolistapp/index.html',context)

def addtodo(request):
    form = TodoForm(request.POST)

    
    new_todo = Todo(text=request.POST['text'])
    new_todo.save()
    return redirect('index')

def completed(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')


def deleteComplete(request):
    Todo.objects.filter(complete = True).delete()
    return redirect('index')