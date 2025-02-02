from rest_framework import serializers
from .models import User , UserProfile
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    
    def validate_username(self,row_username):
        if 5 < len(row_username) <= 120:
            return row_username
        raise serializers.ValidationError("Username must be between 6 and 120.")  

    def validate_password(self,row_password):
        if 7 < len(row_password) <= 25:
            return row_password
        raise serializers.ValidationError("Password must be between 8 and 25.")  
    
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','age','email','is_active','created_at']

    def validate_email(self,row_email):

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', row_email):
            raise serializers.ValidationError("Invalid email format. Email must contain '@'")
        

        if UserProfile.objects.filter(email=row_email).exists():
           raise serializers.ValidationError("Email already exists in the database.")
        return row_email

    def validate_age(self,row_age):
        if 0 < row_age <= 120:
            return row_age
        raise serializers.ValidationError("Age must be between 0 and 120.")  

    
