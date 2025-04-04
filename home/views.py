from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .models import Data
# from .serializers import DataModels


# Create your views here.

@api_view(['GET'])
def getting_data(request):
    if request.method == 'GET':
        print("zgot the statement")
    

@api_view(['POST'])
def sending_data(request):
    if request.method == 'POST':
        print("zgot the statement")
        

@api_view(['PUT'])
def updating(request,id):
    if request.method == 'PUT':
        print("zgot the statement")
        
@api_view(['DELETE'])
def dele(request):
    if request.method == 'DELETE':
        print("zgot the statement")
    
