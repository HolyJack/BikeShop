from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

#   Aunthetication

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            email=validated_data['email'], 
            password=validated_data['password']
            )
        
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def check_user(self, request):
        email = request.data['email']
        password = request.data['password']
        
        if email and password:
            user = authenticate(request=request, username=email, password=password)
            
            if not user:
                raise serializers.ValidationError('Invalid user or password')
        else:
            raise serializers.ValidationError('Email and password are required.')
        
        return user

 
class UserAdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdress
        fields = '__all__'
    


class UserMeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    user_adresses = UserAdressSerializer(many=True)
    
    class Meta:
        model = User
        exclude = [
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions',
            'password'
            ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'