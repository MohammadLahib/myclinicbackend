from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import now

class Employee(models.Model):
   
    firstName   = models.CharField(max_length=100, blank=True, null=True)
    lastName    = models.CharField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True)
    email       = models.EmailField(blank=True, null=True)
    gender_choices =  [
        
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]
    gender         = models.CharField(max_length= 20, choices= gender_choices, default= "OTHER")
    ADMINISTRATOR =  'Administartor'
    DENTIST_ASSISTANT =  'Dentist_Assistant'
    NURSE =  'Nurse'
    SECRETARY = 'Secretary'
    role_choices =  [   
        (ADMINISTRATOR, 'Administartor'),
        (DENTIST_ASSISTANT, 'Dentist_Assistant'),
        (NURSE, 'Nurse'),
        (SECRETARY, 'Secretary'),
    ]
    position=  models.CharField(max_length = 100 , choices=role_choices, null=True)
    FULL_TIME =  'Full Time'
    PART_TIME =  'Part_Time'
    CONTRACT = 'Contract'
  
    employment_type =  [   
        (FULL_TIME , 'Full_Time'),
        (PART_TIME , 'Part_Time'),
        (CONTRACT , 'Contract'),
    ]
    employment =  models.CharField(max_length = 100 , choices=employment_type, null=True)
    E_firstName = models.CharField(max_length=100, blank=True, null=True)
    E_lastName = models.CharField(max_length=100, blank=True, null=True) 
    E_contactNumber = models.CharField(max_length=100, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    password =  models.CharField(max_length=100, blank=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.email
    
    

class Room(models.Model):
    room_name = models.CharField(max_length = 100, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    def __str__(self):
        return self.room_name
    
    

class Operation(models.Model):
    room =  models.ForeignKey(Room, on_delete =  models.CASCADE, default="")
    title = models.CharField(max_length = 200 ,blank= True, null = True)
    cost =  models.DecimalField(max_digits=10, decimal_places=2, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    description =  models.CharField(max_length = 200, blank=True, null= True)
    def __str__(self):
        return self.title
    
    

class Patient(models.Model):
   
    firstName   = models.CharField(max_length=100, blank=True, null=True)
    lastName    = models.CharField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True)
    email       = models.EmailField(blank=True, null=True)
    birthDate   = models.DateField(blank=True, null=True)
    address     = models.CharField(max_length = 50)
    gender_choices =  [
        
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]
    gender         = models.CharField(max_length= 20, choices= gender_choices, default= "OTHER")
    E_firstName = models.CharField(max_length=100, blank=True, null=True)
    E_lastName = models.CharField(max_length=100, blank=True, null=True) 
    E_contactNumber = models.CharField(max_length=100, blank=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    totalBalance = models.DecimalField(max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)
    pendingBalance = models.DecimalField(max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.email
    
    
    

class Appointment(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null= False)
    lastName  = models.CharField(max_length=100, blank=True, null= False)
    date      = models.DateField(default=timezone.now())
    time      = models.TimeField(default=timezone.now())
    email     = models.EmailField(blank=True, null= False)
    operation = models.ForeignKey(Operation, on_delete= models.CASCADE, default="Tooth Extraction", null= False)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.firstName +  " " + self.lastName
    
    

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=False,default=1)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE,null=True)
    visitdate = models.DateField(default=datetime.now)
    medicaments =  models.CharField(max_length=500 , blank=True, null=True)
    notes =  models.CharField(max_length=500 , blank=True, null=True)
    image = models.ImageField(null=True, blank=True,default='/placeholder.png')
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.patient)

class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100)    
    message =  models.CharField(max_length=100) 
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
