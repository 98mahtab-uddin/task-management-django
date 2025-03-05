from django.shortcuts import render
from django.http import HttpResponse

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
