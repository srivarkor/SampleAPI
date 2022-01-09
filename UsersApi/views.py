from .models import User
from UsersApi import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,filters
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class UserApiView(APIView):
    serializer_class = serializers.UserSerializer

    def get(self,request, pk=None, format=None):
        if pk is None:
            return self.getAllUsers(request)
        return self.getUser(request,pk)

    def post(self,request,format=None):
        return self.createUser(request)

    def createUser(self,request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            message = 'Sign up Succesful!!'
            return JsonResponse({'message':message}, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def getUser(self,request,pk):
        try:
            curr_user = User.objects.get(pk=pk)
            user_serializer = serializers.UserSerializer(curr_user)
            return  JsonResponse(user_serializer.data)
        except User.DoesNotExist:
            return JsonResponse({'message': "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def getAllUsers(self,request,pk=None):
        user_serializer = serializers.UserSerializer(User.objects.all(),many=True)
        return JsonResponse(user_serializer.data, safe=False)
