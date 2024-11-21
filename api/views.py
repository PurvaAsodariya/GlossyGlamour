from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from .models import Makeup  # Change this import
from .serializers import MakeupSerializer  # Change this import

class MakeupViewSet(viewsets.ModelViewSet):  # Change class name from FurnitureViewSet to MakeupViewSet
    queryset = Makeup.objects.all()  # Change queryset to Makeup
    serializer_class = MakeupSerializer  # Change serializer_class to MakeupSerializer

class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        # Validate inputs
        if not username or not password or not email:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create user without sending email
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Validate inputs
        if not username or not password:
            return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Log out the user
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_205_RESET_CONTENT)
