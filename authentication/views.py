from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .serializers import UserRegistrationSerializer, UserLogInSerializer

# Utility function to get JWT tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# User Registration View
class UserRegistrationView(APIView):
    """
    Handles user registration with basic fields.
    """
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {
                    'token': token,
                    'msg': 'Registration Successful!',
                    'user': user.username,
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login View
class UserLogInView(APIView):
    """
    Handles user login with username and password.
    """
    def post(self, request, format=None):
        serializer = UserLogInSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                token = get_tokens_for_user(user)
                return Response(
                    {
                        'token': token,
                        'msg': 'Login Successful!',
                        'user': user.username,
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'errors': {'non_field_errors': ['Invalid username or password.']}},
                    status=status.HTTP_404_NOT_FOUND
                )
