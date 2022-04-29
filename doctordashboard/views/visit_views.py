from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from doctordashboard.models import Visit
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from doctordashboard.serializers import VisitSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import messages
from django.core.files.storage import default_storage
from rest_framework.permissions import IsAdminUser, IsAuthenticated

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getVisits(request):
    visits = Visit.objects.all()
    visit_serializer = VisitSerializer(visits, many=True)
    return Response(visit_serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getVisit(request, pk):
    visits  = Visit.objects.filter(_id=pk)
    serializer = VisitSerializer(visits, many=False)
    return Response(serializer.data)

def getVisitsPatient(request, pk):
    visits  = Visit.objects.get(patient=pk) 
    serializer = VisitSerializer(visits, many=False)
    return JsonResponse(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def postVisit(request):
    # permission_classes = [IsAdminUser]
    visit = JSONParser().parse(request)
    visit_serializer = VisitSerializer(data=visit)
    if visit_serializer.is_valid():
        visit_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def putVisit(request, pk):
    # permission_classes = [IsAdminUser]
    visit = JSONParser().parse(request)
    visit_data = Visit.objects.get(_id=pk)
    visit_serializer = VisitSerializer(visit_data, data=visit)
    if visit_serializer.is_valid():
        visit_serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def deleteVisit(request, pk):
    # permission_classes = [IsAdminUser]
    visit = Visit.objects.get(_id=pk)
    visit.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 

@api_view(['POST'])
#@permission_classes([IsAuthenticated])

def uploadImage(request):
    data = request.data
    visit_id = data['visit_id']
    visit = Visit.objects.get(_id=visit_id)
    visit.image = request.FILES.get('image')
    visit.save()
    
    return JsonResponse('Image was uploaded')