from django.contrib import admin
from django.urls import path
from doctordashboard.views import visit_views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.getVisits, name= "visits"),
    path('patient/<str:pk>/', views.getVisitsPatient, name = "patient-visit"),
    path('create/', views.postVisit, name = "visit-create"),
    path('<str:pk>/',views.getVisit, name = "visit"),
    path('update/<str:pk>/', views.putVisit, name="visit-update"),
    path('delete/<str:pk>/', views.deleteVisit, name="visit-delete"),
]
    