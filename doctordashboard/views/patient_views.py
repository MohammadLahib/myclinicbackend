from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from doctordashboard.models import Patient, Visit
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from doctordashboard.serializers import PatientSerializer, VisitSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import messages
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getPatients(request):
    patients = Patient.objects.all()
    patient_serializer = PatientSerializer(patients, many=True)
    return Response(patient_serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getPatient(request, pk):
    patient = Patient.objects.get(_id=pk)
    serializer = PatientSerializer(patient, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPatientsVisit(request):
    visits  = Visit.objects.all()
    serializer = VisitSerializer(visits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPatientVisit(request, pk):
    visits  = Visit.objects.filter(patient=pk)
    serializer = VisitSerializer(visits, many=True)
    return Response(serializer.data)



@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def postPatient(request):
    # permission_classes = [IsAdminUser]
    patient = JSONParser().parse(request)
    patient_serializer = PatientSerializer(data=patient)
    if patient_serializer.is_valid():
        patient_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
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
#@permission_classes([IsAuthenticated])
def deletePatient(request, pk):
    # permission_classes = [IsAdminUser]
    patient = Patient.objects.get(_id=pk)
    patient.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 