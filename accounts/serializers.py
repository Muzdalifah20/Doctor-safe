from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the basic User model fields.
    """
    class Meta:
        model =  get_user_model()
        fields = ['id', 'username']

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Accepts password as write-only and returns a token on creation.
    """
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)  # Add token field for output

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username', 'password', 'token']

    def create(self, validated_data):
        """
        Creates a new user and generates an authentication token.
        """
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
         
        token = Token.objects.create(user=user)
        user.token = token.key
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Accepts username and password, returns token on successful authentication.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)  # Add token field for output

    def validate(self, data):
        """
        Validates user credentials and returns token if valid.
        """
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            return data
        raise serializers.ValidationError("Invalid credentials")


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving and updating user profile information.
    Includes profile picture.
    """
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'username','profile_picture']