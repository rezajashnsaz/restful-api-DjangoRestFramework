from django.shortcuts import render,HttpResponse
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from articles.models import *
from accounts.api.v1.serializers import *
from rest_framework.decorators import api_view




########
# register user
########
@api_view(['POST'])
def register(request):
    serializers = UserRegisterSerializer(data = request.data)
    if serializers.is_valid(raise_exception = True):
        serializers.save()
        return Response({
            "data": serializers.data , 
            "status": 200 
        })