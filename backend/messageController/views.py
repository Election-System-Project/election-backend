from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics

from extraUserController.models import User
from .models import Message
from .serializers import MessageSerializer

# Create your views here.
@api_view(["POST"])
def add_message(request,*args,**kwargs):
    studentNumber = request.data["studentid"]
    user = User.objects.get(studentNumber = studentNumber)
    content = request.data["content"]
    data = {
        "content": content,
        "user": user
    }
    serializer = MessageSerializer(data=data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(data = {"message": "Message is added"})

@api_view(["POST"])
def get_message(request, *args, **kwargs):
    studentNumber = request.data["studentid"]
    user = User.objects.get(studentNumber = studentNumber)
    qs = Message.objects.all().filter(user = user)
    if qs.exists():
        serializer = MessageSerializer(qs, many = True).data
        return Response(data=serializer)
    return Response(data = {"data": []})