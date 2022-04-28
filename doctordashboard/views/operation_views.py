from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from doctordashboard.models import Operation
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from doctordashboard.serializers import OperationSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import messages
from django.core.files.storage import default_storage
from rest_framework.permissions import IsAdminUser, IsAuthenticated





@api_view(['GET'])
#@permission_classes([IsAuthenticated])

def getOperations(request):
    operations = Operation.objects.all()
    operation_serializer = OperationSerializer(operations, many=True)
    return Response(operation_serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getOperation(request, pk):
    operations = Operation.objects.get(_id=pk)
    serializer = OperationSerializer(operations, many=False)
    return Response(serializer.data)






@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def postOperation(request):
    # permission_classes = [IsAdminUser]
    operation = JSONParser().parse(request)
    operation_serializer = OperationSerializer(data=operation)
    if operation_serializer.is_valid():
        operation_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
#@permission_classes([IsAuthenticated])

def putOperation (request, pk):
    # permission_classes = [IsAdminUser]
    operation = JSONParser().parse(request)
    operation_data = Operation.objects.get(_id=pk)
    operation_serializer = OperationSerializer(operation_data, data=operation)
    if operation_serializer.is_valid():
        operation_serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])

def deleteOperation(request, pk):
    # permission_classes = [IsAdminUser]
    operation = Operation.objects.get(_id=pk)
    operation.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 
