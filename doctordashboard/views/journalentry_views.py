from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from doctordashboard.models import PaymentJournal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from doctordashboard.serializers import PaymentJournalSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib import messages
from django.core.files.storage import default_storage
from rest_framework.permissions import IsAdminUser, IsAuthenticated



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getJournals(request):
    journals = PaymentJournal.objects.all()
    journal_serializer = PaymentJournalSerializer(journals, many=True)
    return Response(journal_serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getJournal(request, pk):
    journals = PaymentJournal.objects.filter(_id=pk)
    serializer = PaymentJournalSerializer(journals, many=True)
    return Response(serializer.data)



@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def postJournal(request):
    journal = JSONParser().parse(request)
    journal_serializer = PaymentJournalSerializer(data=journal)
    if journal_serializer.is_valid():
        journal_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def putJournal(request, pk):
    journal = JSONParser().parse(request)
    journal_data = PaymentJournal.objects.get(_id=pk)
    journal_serializer = PaymentJournalSerializer(journal_data, data=journal)
    if journal_serializer.is_valid():
        journal_serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def deleteJournal(request, pk):
    journal = PaymentJournal.objects.get(_id=pk)
    journal.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 
