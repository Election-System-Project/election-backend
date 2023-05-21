from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework import status

# Create your views here.
class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

create_user_view = CreateUserView.as_view()

class LoginView(generics.GenericAPIView):
    serializer_class = ObtainAuthToken.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request=request,
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'email': f"{user.email}", 'role': f"{user.role}"})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

login_view = LoginView.as_view()