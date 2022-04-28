# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from doctordashboard.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from doctordashboard.serializers import UserSerializer
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from django.contrib import messages
# from django.core.files.storage import default_storage
# from rest_framework.permissions import IsAdminUser





# @api_view(['GET'])
# def getemployees(request):
#     employees = User.objects.all()
#     employee_serializer = UserSerializer(employees, many=True)
#     return Response(employee_serializer.data)


# @api_view(['GET'])
# def getemployee(request, pk):
#     employees = User.objects.get(_id=pk)
#     serializer = UserSerializer(employees, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def postemployee(request):
#     # permission_classes = [IsAdminUser]
#     employee = JSONParser().parse(request)
#     employee_serializer = UserSerializer(data=operation)
#     if employee_serializer.is_valid():
#         employee_serializer.save()
#         return Response("Added Successfully!!", safe=False)
#     return Response("Failed to Add.", safe=False)

# @api_view(['PUT'])
# def putemployee(request, pk):
#     # permission_classes = [IsAdminUser]
#     employee = JSONParser().parse(request)
#     employee_data = App.objects.get(_id=pk)
#     employee_serializer = UserSerializer(employee_data, data=employee)
#     if employee_serializer.is_valid():
#         employee_serializer.save()
#         return Response("Updated Successfully!!", safe=False)
#     return Response("Failed to Update.", safe=False)
   
# @api_view(['DELETE'])
# def deleteemployee(request, pk):
#     # permission_classes = [IsAdminUser]
#     employee = User.objects.get(_id=pk)
#     User.delete()
#     return Response('"Deleted Succeffully!!", safe=False') 
