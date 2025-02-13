from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style = 'color: red>Welcome to the Task Management System</h1>")
def contact(request):
    return HttpResponse("<h1 style = 'color: red'>This is Contact Page</h1>")
def show_task(request):
    return HttpResponse("<h1 style = 'color: red'>This is Task Page</h1>")