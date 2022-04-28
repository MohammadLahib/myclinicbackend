from django.urls import re_path
from django.contrib import admin
from django.urls import path
from doctordashboard.views import room_views as views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.getRooms, name = "rooms"),
    path('create/', views.postRoom, name = "room-create"),
    path('<str:pk>/', views.getRoom, name="room"),
    path('update/<str:pk>/', views.putRoom, name="room-update"),
    path('delete/<str:pk>/', views.deleteRoom, name="room-delete")
   
] 
