from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vote
from .serializers import VoteSerializer

class VoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class VoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    lookup_field = 'id'

@api_view(["POST"])
def add_vote(request):
    if request.method == 'POST':
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            candidate_name = serializer.validated_data['candidate_name']
            try:
                vote = Vote.objects.get(candidate_name=candidate_name)
                vote.count += 1
                vote.save()
            except Vote.DoesNotExist:
                vote = Vote(candidate_name=candidate_name, count=1)
                vote.save()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'status': 'error', 'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

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