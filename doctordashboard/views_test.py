from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Patient, Appointment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . serializers import PatientSerializer, AppointmentSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import messages
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse



@api_view(['GET'])
def getPatients(request):
    patients = Patient.objects.all()
    patient_serializer = PatientSerializer(patients, many=True)
    return Response(patient_serializer.data)


@api_view(['GET'])
def getPatient(request, pk):
    patient = Patient.objects.get(_id=pk)
    serializer = PatientSerializer(patient, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postPatient(request):
    # permission_classes = [IsAdminUser]
    patient = JSONParser().parse(request)
    patient_serializer = PatientSerializer(data=patient)
    if patient_serializer.is_valid():
        patient_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
def putPatient(request, pk):
    # permission_classes = [IsAdminUser]
    patient = JSONParser().parse(request)
    patient_data = Patient.objects.get(_id=pk)
    patient_serializer = PatientSerializer(patient_data, data=patient)
    if patient_serializer.is_valid():
        patient_serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
def deletePatient(request, pk):
    # permission_classes = [IsAdminUser]
    patient = Patient.objects.get(_id=pk)
    Patient.delete()
    return Response('"Deleted Succeffully!!", safe=False') 
    
# def index(request, *args, **kwargs):
#     return render(request, 'index.html')


# @api_view(['GET', 'POST'])
# def patient(request):
#     if request.method == 'GET':
#         patient = Patient.objects.all()
#         patient_serializer = PatientSerializer(patient, many=True)
#         return JsonResponse(patient_serializer.data, safe=False)

#     elif request.method == 'POST':
#         patient = JSONParser().parse(request)
#         patient_serializer = PatientSerializer(data=patient)
#         if patient_serializer.is_valid():
#             patient_serializer.save()
#             return JsonResponse("Added Successfully!!", safe=False)
#         return JsonResponse("Failed to Add.", safe=False)

    # elif request.method == 'PUT':
    #     patient = JSONParser().parse(request)
    #     patient_data = Patient.objects.get(pk=patient['PatientID'])
    #     patient_serializer = PatientSerializer(patient_data, data=patient)
    #     if patient_serializer.is_valid():
    #         patient_serializer.save()
    #         return JsonResponse("Updated Successfully!!", safe=False)
    #     return JsonResponse("Failed to Update.", safe=False)

    # elif request.method == 'DELETE':
    #     patient = Patient.objects.get(pk=pk)
    #     patient.delete()
    #     return JsonResponse("Deleted Succeffully!!", safe=False)

# @api_view(['GET', 'PUT', 'DELETE'])
# def patient_detail(request, pk):
#     try:
#         patient =  Patient.objects.get(pk=pk)
        
#     except Patient.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer =  PatientSerializer(patient)
#         return JsonResponse(patient_serializer.data, safe=False)
    
#     elif request.method == 'PUT':
#         patient = JSONParser().parse(request)
#         patient_serializer = PatientSerializer(patient, data=patient)
#         if patient_serializer.is_valid():
#             patient_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=  False)
    
#     elif request.method == 'DELETE':
#         patient.delete()
#         return HttpResponse(status=204)
        

# def user(request, id = 0):
#     if request.method == 'GET':
#         patient = Patient.objects.all()
#         patient_serializer = PatientSerializer(patient, many=True)
#         return JsonResponse(patient_serializer.data, safe=False)

#     elif request.method == 'POST':
#         patient = JSONParser().parse(request)
#         patient_serializer = PatientSerializer(data=patient)
#         if patient_serializer.is_valid():
#             patient_serializer.save()
#             return JsonResponse("Added Successfully!!", safe=False)
#         return JsonResponse("Failed to Add.", safe=False)

#     elif request.method == 'PUT':
#         patient = JSONParser().parse(request)
#         patient_data = Patient.objects.get(patientid=patient['PatientID'])
#         patient_serializer = PatientSerializer(patient_data, data=patient)
#         if patient_serializer.is_valid():
#             patient_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method == 'DELETE':
#         patient = Patient.objects.get(patientid=id)
#         patient.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)






@api_view(['GET'])
def getAppointments(request):
    appointments = Appointment.objects.all()
    appointment_serializer = AppointmentSerializer(appointments, many=True)
    return Response(appointment_serializer.data)


@api_view(['GET'])
def getAppointment(request, pk):
    apppointments = Appointment.objects.get(_id=pk)
    serializer = AppointmentSerializer(apppointments, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postAppointment(request):
    # permission_classes = [IsAdminUser]
    appointment = JSONParser().parse(request)
    appointment_serializer = AppointmentSerializer(data=appointment)
    if appointment_serializer.is_valid():
        appointment_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
def putAppointment(request, pk):
    # permission_classes = [IsAdminUser]
    appointment = JSONParser().parse(request)
    appointment_data = App.objects.get(_id=pk)
    appointment_serializer = AppointmentSerializer(patient_data, data=patient)
    if appointment_serializer.is_valid():
        appointment_serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
def deleteAppointment(request, pk):
    # permission_classes = [IsAdminUser]
    appointment = Appointment.objects.get(_id=pk)
    Appointment.delete()
    return Response('"Deleted Succeffully!!", safe=False') 



def index(request):
    return  HttpResponse("Welcome")



# @csrf_exempt
# def Appointment(request, id=0):
#     if request.method == 'GET':
#         appointment = Appointment.objects.all()
#         appointment_serializer = Appo(appointment, many=True)
#         return JsonResponse(appointment_serializer.data, safe=False)

#     elif request.method == 'POST':
#         appointment_data = JSONParser().parse(request)
#         appointment_serializer = AppointmentSerializer(data=employee_data)
#         if appointment_serializer.is_valid():
#             appointment_serializer.save()
#             return JsonResponse("Added Successfully!!", safe=False)
#         return JsonResponse("Failed to Add.", safe=False)

#     elif request.method == 'PUT':
#         appointment_data = JSONParser().parse(request)
#         appointment = Appointment.objects.get(
#             EmployeeId=employee_data['EmployeeId'])
#         appointment_serializer = AppointmentSerializer(
#             appointment, data=appointment_data)
#         if appointment_serializer.is_valid():
#             appointment_serializer.save()
#             return JsonResponse("Updated Successfully!!", safe=False)
#         return JsonResponse("Failed to Update.", safe=False)

#     elif request.method == 'DELETE':
#         appointment = Appointment.objects.get(EmployeeId=id)
#         appointment.delete()
#         return JsonResponse("Deleted Succeffully!!", safe=False)


# # @csrf_exempt
# # def SaveFile(request):
# #     file=request.FILES['myFile']
# #     file_name = default_storage.save(file.name,file)

# #     return JsonResponse(file_name,safe=False)


# # Create your views here.

# def HomePage(request):
#     return render(request, 'index.html')


# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = CreateUserForm()
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)

#                 return redirect('loginpage')

#         context = {'form': form}
#         return render(request, 'register.html', context)


# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.info(request, 'Username OR password is incorrect')

#         context = {}
#         return render(request, 'login.html', context)


# def logOut(request):
#     logout(request)
#     return redirect('loginpage')


# def dentistDashboard(request):
#     return render(request, 'dentistdashboard.html')

# def addpatient(request):
#     if request.method == 'POST':
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()


# def patientlist(request):
#     patients_list = Patient.objects.all()
#     context = {
#         'patients_list': patients_list,
#     }
#     return render(request, 'patientlist.html', context)


# def addappointment(request):
#     form = AppointmentForm()

#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()

#     context = {'form': form}

#     return render(request, 'addappointment.html', context)

# @api_view(['GET', 'PUT', 'DELETE'])
# @api_view(['POST'])
# def createpatient(request):
#     serializer =  PatientSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# # @login_required(login_url='login')
# def appointmentslist(request):
#     appointmentslist = Appointment.objects.all()
#     context = {
#         'appointmentslist': appointmentslist,
#     }
#     # requet and response
#     return render(request, 'appointmentslist.html', context)


# # @login_required(login_url='login')
# def showform(request):
#     form = FormContactForm(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context = {'form': form}

#     return render(request, 'contactform.html', context)
