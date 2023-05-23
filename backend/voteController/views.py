from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from candidateController.models import Candidate
from .serializers import VoteSerializer
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
    serializer = VoteSerializer(data=request.data)
    if request.data["student_id"] == "-1": 
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    if serializer.is_valid():
        student_id = serializer.validated_data['student_id']
        try:
            vote = Candidate.objects.get(student_id=student_id)
            vote.vote_count += 1
            vote.save()
        except Candidate.DoesNotExist:
            
            return Response({'status': 'failure', 'error': 'Candidate does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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