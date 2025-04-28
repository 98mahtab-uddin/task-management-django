from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task,TaskDetail,Project
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg

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
    #task_count = Task.objects.aggregate(num_task = Count('id'))
    projects = Project.objects.annotate(num_task = Count('task')).order_by('num_task')
    return render(request,"show_task.html",{"projects":projects})