from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Data
from .serializers import DataModels


# Create your views here.

@api_view(['GET'])
def getting_data(request):
    if request.method == 'GET':
        data = Data.objects.all()
        serializers = DataModels(data,many=True)
        return Response(serializers.data)
    

@api_view(['POST'])
def sending_data(request):
    if request.method == 'POST':
        serializers = DataModels(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        

@api_view(['PUT'])
def updating(request,id):
    if request.method == 'PUT':
        data = Data.objects.get(id=id)
        serializers = DataModels(data,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
        
@api_view(['DELETE'])
def dele(request):
    if request.method == 'DELETE':
        data = Data.objects.all()
        data.delete()
        return Response(status=status.HTTP_200_OK)
    
