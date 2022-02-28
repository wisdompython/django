from django.contrib import admin
from django.urls import path
from . import views
from .views import TaskListView, TaskCreateView,TaskUpdateView,TaskDeleteView, CustomLoginView, CustomLogoutView




urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name ='users/login.html'), name = 'login'),
    path('logout/', CustomLogoutView.as_view(template_name ='users/logout.html', next_page= 'login'), name = 'logout'),
    path('signup/', views.SignUp, name = 'signup'),
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskUpdateView.as_view(), name = 'edit'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name = 'delete'),
    path('addtask/', TaskCreateView.as_view(), name='Task-Creation'),
]