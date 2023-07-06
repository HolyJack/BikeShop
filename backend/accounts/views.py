from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class UserRegisterView(APIView):
    serializer = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        data = request.data
        serializer = self.serializer(data=data)
        
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        email = data['email']
        if not data['email'] or User.objects.filter(email=email).exists():
            return Response({'email': [
                'User already exists'
                ]}, status=status.HTTP_400_BAD_REQUEST)
    
        serializer.create(data)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    serializer = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [SessionAuthentication]
    
    def post(self, request):
        data = request.data
        serializer = self.serializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(request)
            login(request, user)
            
            return Response({'message': 'Login succesful.'}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserMeView(APIView):
    serializer_class = UserMeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request):
        serializer = self.serializer_class(request.user, data=request.data)
        if serializer.is_valid():
            serializer.update(request.user, validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAdressesView(APIView):
    pass
