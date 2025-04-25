from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task,TaskDetail,Project
from datetime import date
from django.db.models import Q

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
    # Select releted (ForeignKey,OneToOneField)
    # tasks = Task.objects.select_related('details').all()
    #tasks = TaskDetail.objects.select_related('task').all()
    #tasks = Task.objects.select_related('project').all()
    
    # prefetch_releted(reverse foreign key, many to many)

    #tasks = Project.objects.prefetch_related('task_set').all()
    tasks = Task.objects.prefetch_related('assigned_to').all()

    return render(request,"show_task.html",{"tasks":tasks})