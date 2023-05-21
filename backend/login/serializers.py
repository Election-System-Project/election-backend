from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 
                  'student_number', 
                  'grade', 
                  'auth_token',
                  'expires_after',
                  'email'
                  ]