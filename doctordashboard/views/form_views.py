from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from doctordashboard.models import Form
from doctordashboard.serializers import FormSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.permissions import IsAdminUser, IsAuthenticated




@api_view(['GET'])

def getForms(request):
    forms = Form.objects.all()
    form_serializer = FormSerializer(forms, many=True)
    return JsonResponse(form_serializer.data , safe=False)


@api_view(['GET'])
def getForm(request, pk):
    forms = Form.objects.get(_id=pk)
    serializer = FormSerializer(forms, many=False)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def postForm(request):
    # permission_classes = [IsAdminUser]
    form = JSONParser().parse(request)
    form_serializer = FormSerializer(data=form)
    if form_serializer.is_valid():
        form_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
def putForm (request, pk):
    # permission_classes = [IsAdminUser]
    form = JSONParser().parse(request)
    form_data = Form.objects.get(_id=pk)
    form_serializer = FormSerializer(form_data, data=form)
    if form_serializer.is_valid():
        form_serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
def deleteForm(request, pk):
    # permission_classes = [IsAdminUser]
    form = Form.objects.get(_id=pk)
    form.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 
