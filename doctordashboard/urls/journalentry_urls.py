from django.contrib import admin
from django.urls import path
from doctordashboard.views import journalentry_views as views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.getJournals, name = "journals"),
    path('create/', views.postJournal, name = "journal-create"),
    path('<str:pk>/', views.getJournal, name="journal"),
    path('update/<str:pk>/', views.putJournal, name="journal-update"),
    path('delete/<str:pk>/', views.deleteJournal, name="journal-delete")
] 
