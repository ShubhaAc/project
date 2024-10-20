from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser  # Ensure this import is correct

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid username or password.")
            data['user'] = user
        else:
            raise serializers.ValidationError("Must include both username and password.")
        
        return data
