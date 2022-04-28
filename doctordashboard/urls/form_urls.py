from django.contrib import admin
from django.urls import path
from doctordashboard.views import form_views as views



urlpatterns = [
    path('', views.getForms, name = "forms"),
    path('create/', views.postForm, name = "form-create"),
    path('<str:pk>/', views.getForm, name="formr"),
    path('update/<str:pk>/', views.putForm, name="form-update"),
    path('delete/<str:pk>/', views.deleteForm, name="form-delete")
   
] 
