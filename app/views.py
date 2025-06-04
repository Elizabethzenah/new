from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Person
from app.serializer import PersonSerializer


# Create your views here.

@api_view(['GET'])
def fetch(request):
    users = Person.objects.all()
    serializer = PersonSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return None


# ngrok http --urls=mature-octopus-casual.ngrok.free