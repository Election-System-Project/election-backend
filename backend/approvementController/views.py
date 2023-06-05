from rest_framework import request, generics,status 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from candidateController.models import Candidate
from .serializers import ApprovementSerializer, ResultSerializer

# Create your views here.
@api_view(["POST","GET"])
def result_list_view(request, *args, **kwargs):
    qs = Candidate.objects.all().filter(is_approved= True)
    result_data = ResultSerializer(qs, many = True).data
    
    return Response(data=result_data)

@api_view(["POST","GET"])
def approvement_list_view(request, *args, **kwargs):
    qs = Candidate.objects.all().filter(is_winner = False)
    result_data = ResultSerializer(qs, many = True).data
    filtered_data = []
    for data in result_data:
        if data["has_most_counts"]: 
            filtered_data.append(data)
    return Response(data=filtered_data)

@api_view(["POST"])
def result_approve_view(request, *args, **kwargs):
    student_id = ""
    print(request.data)
    for student in request.data:
        try:
            student_id = student["student_id"]
            candidate = Candidate.objects.get(student_id=student_id)
            candidate.is_winner = True
            candidate.is_approved = True
            candidate.save()
        except Candidate.DoesNotExist:
            return Response({'status': 'failure', 'error': f'Candidate with {student_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'status': 'success'})

@api_view(["POST"])
def result_reject_view(request, *args, **kwargs):
    student_id = ""
    print(request.data)
    for student in request.data:
        try:
            student_id = student["student_id"]
            candidate = Candidate.objects.get(student_id=student_id)
            candidate.is_approved = False
            candidate.is_winner = False
            candidate.save()
        except Candidate.DoesNotExist:
            return Response({'status': 'failure', 'error': f'Candidate with {student_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'status': 'success'})