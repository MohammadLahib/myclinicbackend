from django.urls import re_path
from django.contrib import admin
from django.urls import path
from doctordashboard.views import patient_views as views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.getPatients, name = "patients"),
    path('create/', views.postPatient, name = "patient-create"),
    path('visits/', views.getPatientsVisit, name = "patients-visits"),
    path('visits/<str:pk>/', views.getPatientVisit, name = "patient-visit"),
    path('<str:pk>/', views.getPatient, name="patient"),
    path('update/<str:pk>/', views.putPatient, name="patient-update"),
    path('delete/<str:pk>/', views.deletePatient, name="patient-delete")
] 
