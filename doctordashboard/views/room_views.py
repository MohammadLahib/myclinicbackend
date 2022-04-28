from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from doctordashboard.models import Room
from doctordashboard.serializers import RoomSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAdminUser



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getRooms(request):
    rooms = Room.objects.all()
    room_serializer = RoomSerializer(rooms, many=True)
    return Response(room_serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getRoom(request, pk):
    rooms = Room.objects.get(_id=pk)
    serializer = RoomSerializer(rooms, many=False)
    return Response(serializer.data)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def postRoom(request):
    # permission_classes = [IsAdminUser]
    room = JSONParser().parse(request)
    room_serializer = RoomSerializer(data=room)
    if room_serializer.is_valid():
        room_serializer.save()
        return JsonResponse("Added Successfully!!", safe=False)
    return JsonResponse("Failed to Add.", safe=False)

@api_view(['PUT'])
#@permission_classes([IsAuthenticated])
def putRoom(request, pk):
    # permission_classes = [IsAdminUser]
    room = JSONParser().parse(request)
    room_data = Room.objects.get(_id=pk)
    room_serializer = RoomSerializer(room_data, data=room)
    if room_serializer.is_valid():
        room_serializer.save()
        return JsonResponse("Updated Successfully!!", safe=False)
    return JsonResponse("Failed to Update.", safe=False)
   
@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def deleteRoom(request, pk):
    # permission_classes = [IsAdminUser]
    room = Room.objects.get(_id=pk)
    room.delete()
    return JsonResponse("Deleted Succeffully!!", safe=False) 
