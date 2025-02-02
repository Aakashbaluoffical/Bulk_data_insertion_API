from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User,UserProfile
from .serializer import UserSerializer , UserProfileSerializer
from rest_framework import generics  
from django.http import JsonResponse
import pandas as pd 
import csv
import io
# Create your views here.

print("open View.py")




class GetAllData(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer







class UploadCSV(APIView):

    
    def post(self,request,*args,**kwargs):

        data = request.FILES.get('file')
        
        if not data:
            return JsonResponse({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse({"Sucessfull": "File got it!"}, status=status.HTTP_200_OK)
        try:
            decoded_file =  data.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(decoded_file))
        except  Exception as e:
            return JsonResponse({"error": "Only supports .CSV files"}, status=status.HTTP_400_BAD_REQUEST)

        errors = []
        
        valid_users = []

        for row in  reader:
            
            user_profile_data = {
                    "first_name" : row.get("first_name"),
                    "last_name" : row.get("last_name"),
                    "age" : row.get("age"),
                    "email" : row.get("email"),
                    "is_active" : True
                    
            }
            user_data = {
                    "username" : row.get('username'),
                    "password" : row.get('password')
                   
            }
            print("user_profile_datauser_profile_datauser_profile_data",user_profile_data)
            print("user_datauser_data",user_data)
            print("errorserrors,",errors)
            #  {'first_name': 'William', 'last_name': 'Santiago', 'age': '25', 'email': 'williamsantiago@gmail.com', 'is_active': True}
                # {'username': 'williamsantiago', 'password': '1fncdnru'}


            

            
            user_profile_serializer = UserProfileSerializer(data=user_profile_data)
            user_serializer = UserSerializer(data={**user_data})

           
            if  user_profile_serializer.is_valid() and user_serializer.is_valid():
            # if  user_profile_serializer.is_valid() :

                user_profile = user_profile_serializer.save()                      
            else:
                errors.append({"row": row, "errors": user_profile_serializer.errors})
                continue



            # user_serializer = UserSerializer(data={**user_data, "user_profile": user_profile.id})

           
            if  user_serializer.is_valid():
                valid_users.append(User(
                    username=user_data["username"], 
                    password=user_data["password"], 
                    user_profile=user_profile
                ))

            else:
                errors.append({"row": row, "errors": user_serializer.errors})
                continue


            print("valid_users",valid_users)
            if valid_users:
                User.objects.bulk_create(valid_users)
                valid_users.pop()
                

        
        return JsonResponse({"Data": "Inserted !"}, status=status.HTTP_200_OK)

