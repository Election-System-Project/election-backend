from rest_framework import generics, mixins

from .models import User
from .serializers import UserSerializer, VoterSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST","GET"])
def user_list_view(request, *args, **kwargs):
    qs = User.objects.all()
    result_data = UserSerializer(qs, many = True).data
    
    return Response(data=result_data)


@api_view(["POST"])
def user_create_view(request, *args, **kwargs):
    data = {
        "name": request.data["name"],
        "surname": request.data["surname"],
        "studentNumber": request.data["studentNumber"]
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({
            "statusMessage": "User added successfully"
        })
    
@api_view(["POST"])
def user_vote_view(request, *args, **kwargs):
    serializer = VoterSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        studentNumber = request.data["studentNumber"]
        vote = User.objects.get(studentNumber=studentNumber)
        vote.hasVoted = True
        vote.save()
        return Response(data = {
            "messageStatus": "Successfully changed vote"
        }
        )
    


    
    


