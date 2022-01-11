from .models import User
from .serializers import UserSerializer
from django.core import serializers as spserial
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets,filters, generics, status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class UserApiView(APIView):

    def get(self,request, pk=None, format=None):
        return self.getUser(request,pk)

    def post(self,request,format=None):
        return self.createUser(request)

    def put(self,request,pk=None,format=None):
        return self.updateUser(request,pk)

    def delete(self,request,pk=None,format=None):
        return self.deleteUser(request,pk)

    def createUser(self,request):
        new_user = request.data.get('user')
        user_serializer = UserSerializer(data = new_user)
        if user_serializer.is_valid(raise_exception=True):
            saved_user = user_serializer.save()
            message = 'Sign up Succesful!!'
            return JsonResponse({'message':message,'id':user_serializer.data['id'],'firstName':user_serializer.data['firstName']},status = status.HTTP_201_CREATED)
        return JsonResponse(status = status.HTTP_400_BAD_REQUEST)

    def getUser(self,request,pk):
        if pk is None:
            return JsonResponse({'message': "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        try:
            curr_user = User.objects.get(pk=pk)
            user_serializer = UserSerializer(curr_user)
            return  JsonResponse(user_serializer.data)
        except User.DoesNotExist:
            return JsonResponse({'message': "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def updateUser(self,request,pk):
        curr_user = get_object_or_404(User.objects.all(), pk=pk)
        new_data = request.data.get('user')
        user_serializer = UserSerializer(instance=curr_user, data=new_data, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            message = 'Update Succesful!!'
            return JsonResponse({'user':user_serializer.data,'message':message}, status = status.HTTP_200_OK)

    def deleteUser(self,request,pk):
        del_user = get_object_or_404(User.objects.all(), pk=pk)
        del_user.delete()
        message = 'Account Deleted!!!'
        return JsonResponse({'message':message}, status = status.HTTP_200_OK)


class UserApiAdminView(APIView):

    def get(self,request, pk=None, format=None):
        return self.getUser(request,pk)

    def post(self,request,format=None):
        return self.createUser(request)

    def put(self,request,pk=None,format=None):
        return self.updateUser(request,pk)

    def delete(self,request,pk=None,format=None):
        return self.deleteUser(request,pk)

    def createUser(self,request):
        new_user = request.data.get('user')
        user_serializer = UserSerializer(data = new_user)
        if user_serializer.is_valid(raise_exception=True):
            saved_user = user_serializer.save()
            message = 'User creation succesful!!'
            return JsonResponse({'message':message,'user':user_serializer.data},status = status.HTTP_201_CREATED)
        return JsonResponse(status = status.HTTP_400_BAD_REQUEST)

    def getUser(self,request,pk):
        if pk is None:
            return JsonResponse({'message': "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        try:
            curr_user = User.objects.get(pk=pk)
            user_serializer = UserSerializer(curr_user)
            return  JsonResponse(user_serializer.data)
        except User.DoesNotExist:
            return JsonResponse({'message': "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def updateUser(self,request,pk):
        curr_user = get_object_or_404(User.objects.all(), pk=pk)
        new_data = request.data.get('user')
        user_serializer = UserSerializer(instance=curr_user, data=new_data, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            message = 'Update Succesful!!'
            return JsonResponse({'user':user_serializer.data,'message':message}, status = status.HTTP_200_OK)

    def deleteUser(self,request,pk):
        del_user = get_object_or_404(User.objects.all(), pk=pk)
        del_user.delete()
        message = 'User Deleted!!!'
        return JsonResponse({'message':message}, status = status.HTTP_200_OK)


class UserApiAdminSearchUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['firstName', 'lastName','phoneNumber','email','category']
