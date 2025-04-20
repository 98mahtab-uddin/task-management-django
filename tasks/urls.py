from django.urls import path
# from .views import show_task
from tasks.views import dashbord,user_dashbord,manager_dashbord,test,create_task,view_task

urlpatterns = [
    path('dashbord/',dashbord),
    path('user-dashbord/',user_dashbord),
    path('manager-dashbord/',manager_dashbord),
    path('test/',test),
    path('create_task/',create_task),
    path('view_task/',view_task)
]