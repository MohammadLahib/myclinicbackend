from django.contrib import admin
from django.urls import path
from doctordashboard.views import appointment_views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.getAppointments, name= "appointments"),
    path('create/', views.postAppointment, name = "appointment-create"),
    path('<str:pk>/',views.getAppointment, name = "appointment"),
    path('update/<str:pk>/', views.putAppointment, name="appointment-update"),
    path('delete/<str:pk>/', views.deleteAppointment, name="appointment-delete"),
]
