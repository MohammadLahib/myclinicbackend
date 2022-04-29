from django.urls import re_path
from django.contrib import admin
from django.urls import path
from doctordashboard.views import employee_views as views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.getemployees, name = "employees"),
    path('create/', views.postemployee, name = "employee-create"),
    path('<str:pk>/', views.getemployee, name="employee"),
    path('update/<str:pk>/', views.postemployee, name="employee-update"),
    path('delete/<str:pk>/', views.deleteemployee, name="employee-delete")
   
] 
