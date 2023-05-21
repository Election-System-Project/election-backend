from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
import secrets
# Create your views here.

@api_view(["POST"])
def login_view(request, *args, **kwargs):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = User.objects.get(email=email, password=password)
    except User.DoesNotExist:
        return Response({'error': 'Invalid email or password'}, status=400)

    
    token = secrets.token_hex(32)
    user.auth_token = token
    user.save()

    serializer = UserSerializer(user)
    return Response(serializer.data, status=200)