from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Patient, Appointment, Operation, Room, Visit, PaymentJournal, Form , PaymentJournal
from django.contrib.auth.models import Group

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Room)
admin.site.register(Operation)
admin.site.register(Visit)
admin.site.register(Form)
admin.site.register(PaymentJournal)