from rest_framework import request, generics,status 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from candidateController.models import Candidate
from candidateController.serializers import CandidateModelSerializer

# Create your views here.
@api_view(["POST","GET"])
def result_list_view(request, *args, **kwargs):
    qs = Candidate.objects.all().filter(is_winner= False)
    result_data = CandidateModelSerializer(qs, many = True).data
    
    return Response(data=result_data)

@api_view(["POST"])
def result_approve_view(request, *args, **kwargs):
    student_id = ""
    for id in request.data["studentIds"]:
        try:
            candidate = Candidate.objects.get(student_id=student_id)
            candidate.is_winner = True
            candidate.save()
        except Candidate.DoesNotExist:
            return Response({'status': 'failure', 'error': f'Candidate with {student_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'status': 'success'})

@api_view(["POST"])
def result_reject_view(request, *args, **kwargs):
    student_id = ""
    for id in request.data["studentIds"]:
        try:
            candidate = Candidate.objects.get(student_id=student_id)
            candidate.is_rejected = True
            candidate.save()
        except Candidate.DoesNotExist:
            return Response({'status': 'failure', 'error': f'Candidate with {student_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'status': 'success'})