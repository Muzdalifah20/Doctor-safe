from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserSerializer
from django.contrib.auth import authenticate
from .models import CustomUser
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator

class RegisterView(APIView):
    """
    API endpoint for registering a new user.
    Allows any user to access.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Registers a new user and returns their profile and auth token.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserProfileSerializer(user).data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    API endpoint for user login.
    Allows any user to access.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Authenticates a user and returns an auth token and profile data.
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user': UserProfileSerializer(user).data
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    API endpoint to logout a user by deleting their auth token.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Deletes the user's authentication token (logs them out).
        """
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)

@method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True), name='dispatch')
class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update or delete the authenticated user's profile.
    Requires authentication.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Returns the current authenticated user instance.
        """
        return self.request.user

 
  
 