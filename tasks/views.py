from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task

# Create your views here.
def home(request):
    return render(request,"home.html")
def dashbord(request):
    return render(request,"dashbord/dashbord.html")
def user_dashbord(request):
    return render(request,"dashbord/user-dashbord.html")
def manager_dashbord(request):
    return render(request,"dashbord/manager-dashbord.html")
def test(request):
    names =['rafi','nafi','safi']
    count = 0
    for name in names:
        count += 1
    
    context = {
        "names":names,
        "age": 32,
        "count": count
    }
    return render(request,'test.html',context)

def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm()  # for get
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            '''for django model form data'''
            form.save()
            return render(request,"task_form.html",{"form":form,"message":"Task added successfully"})

    context = {"form":form}
    return render(request,"task_form.html",context)

def view_task(request):
    # retrive all data from tasks model
    tasks = Task.objects.all()

    # retrive a specefic data
    task_3 = Task.objects.get(id=1)
    
    # fetch the first task
    first_task = Task.objects.first()

    return render(request,"show_task.html",{"tasks":tasks, "task3": task_3,"first_task":first_task})