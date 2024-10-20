from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import LoginSerializer

@api_view(['POST'])
def login_view(request):
  if request.method == 'POST':
    serializer = LoginSerializer(data=request.data)
    
    if serializer.is_valid():
      user = serializer.validated_data['user']
      login(request, user)  # Log the user in
      
      # Generate or retrieve the token
      token, created = Token.objects.get_or_create(user=user)
      
      # Redirect logic for mentor/mentee based on user type
      if user.is_mentor:
        # Redirect to the mentor dashboard
        response_data = {
            'token': token.key,
            'user_type': 'mentor',
            'username': user.username,
            'redirect_url': '/api/myapp/dashboard/mentor'  # URL for mentor dashboard
          }
      elif user.is_mentee:
        # Redirect to the mentee dashboard
        response_data = {
            'token': token.key,
            'user_type': 'mentee',
            'username': user.username,
            'redirect_url': '/api/myapp/dashboard/mentee'  # URL for mentee dashboard
        }
      else:
        # If the user is neither a mentor nor a mentee
        response_data = {
            'error': 'User type is not defined.'
        }
      return Response(response_data, status=status.HTTP_200_OK)
    
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def mentor_dashboard(request):
  # Logic for retrieving mentor dashboard data
  return Response({"message": "Welcome to the Mentor Dashboard!"})

@api_view(['GET'])
def mentee_dashboard(request):
  # Logic for retrieving mentee dashboard data
  return Response({"message": "Welcome to the Mentee Dashboard!"})