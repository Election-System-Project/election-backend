from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from candidateController.models import Candidate
from .serializers import VoteSerializer
from extraUserController.serializers import VoterSerializer
from extraUserController.models import User
from .models import Vote



class VoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    lookup_field = 'id'

@api_view(["POST"])
def add_vote(request, *args, **kwargs):
    filtered_user_data = {
        "studentNumber": request.data["user_id"]
    }
    filtered_candidate_data = {
        "student_id": request.data["student_id"]
    }
    print(filtered_user_data)
    print(filtered_candidate_data)
    voter_serializer = VoterSerializer(data=filtered_user_data)
    # vote_serializer = VoteSerializer(data=filtered_candidate_data)
    if request.data["student_id"] == "-1" and voter_serializer.is_valid(): 
        user_id = voter_serializer.validated_data["studentNumber"]
        voter = User.objects.get(studentNumber = user_id)
        voter.hasVoted = True
        voter.save()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    if voter_serializer.is_valid() and voter_serializer.is_valid(raise_exception=True):
        user_id = voter_serializer.validated_data["studentNumber"]
        
        try:
            vote = Candidate.objects.get(student_id=request.data["student_id"])
            vote.vote_count += 1
            vote.save()
            voter = User.objects.get(studentNumber = user_id)
            voter.hasVoted = True
            voter.save()
        except Candidate.DoesNotExist:            
            return Response({'status': 'failure', 'error': 'Candidate does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    else:
        return Response(voter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def get_vote_counts(request):
    if request.method == 'GET':
        votes = Vote.objects.all()
        serializer = VoteSerializer(votes, many=True)
        response_data = {
            'status': 'success',
            'data': serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'error', 'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)