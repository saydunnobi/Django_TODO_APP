from django.shortcuts import render , redirect
from .models import *

# Create your views here.


def index(request):
    if request.method =='POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(
                text=text
            )
            return redirect('/')
        
    todo = Todo.objects.all()
    context = {
        'todo': todo
    }    
    return render(request,'index.html',context)

def deletetodo(request , id):
    Todo.objects.get(id=id).delete()
    return redirect('/')

def about(request):
    return render(request,'about.html')
