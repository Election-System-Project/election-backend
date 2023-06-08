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
    filtered_request = request.data["user"]
    print(filtered_request["department"]["name"])
    data = {
        "name": filtered_request["name"],
        "surname": filtered_request["surname"],
        "studentNumber": filtered_request["studentNumber"],
        "grade": filtered_request["grade"],
        "email": filtered_request["email"],
        "department": filtered_request["department"]["name"]
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        if(not User.objects.filter(studentNumber=filtered_request["studentNumber"]).exists()):
            serializer.save()
        
        user = User.objects.get(studentNumber=filtered_request["studentNumber"])
        user_serializer = UserSerializer(user)
        data = {
            "userData": user_serializer.data,
            "roles": filtered_request["roles"]
        }
        return Response(data = data)
  
    
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