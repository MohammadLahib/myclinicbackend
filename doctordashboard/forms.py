from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Patient, Role

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.phone_number=self.cleaned_data.get('phone_number')
        patient.save()
        return user

class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.save()
        return user
    
    
    
    
    
    
    
    
    
    
# class PatientForm(ModelForm):
#     class Meta:
#         model = Patient
#         fields = '__all__'
        
        
# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'


# class AppointmentForm(ModelForm):
    
#     class Meta:
#         model = Appointment
#         fields = '__all__'
        
# class FormContactForm(forms.ModelForm):
    
#     class Meta:
#         model = ContactForm
#         fields = '__all__'
        
# class LoginForm(forms.ModelForm):
    
#     class Meta:
#         model =  Login
#         fields = '__all__'
        
# class CreateUserForm(UserCreationForm):
    
# 	class Meta:
# 		model = User
# 		fields = '__all__'
