from django.contrib import admin
from django.urls import path
from doctordashboard.views import operation_views as views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.getOperations, name = "operations"),
    path('create/', views.postOperation, name = "operation-create"),
    path('<str:pk>/', views.getOperation, name="operation"),
    path('update/<str:pk>/', views.putOperation, name="operation-update"),
    path('delete/<str:pk>/', views.deleteOperation, name="operation-delete")
   
] 
