from rest_framework import generics
from extraUserController.models import User

from .models import Candidate
from .serializers import CandidateModelSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from documentController.models import PDF
from documentController.serializers import PDFSerializer

from extraUserController.models import User
import os
from urllib.parse import unquote
from election_system_316 import settings

from django.http import FileResponse
# Create your views here.



class CandidateDetailsView(generics.RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateModelSerializer
    lookup_field = 'pk'

candidate_details_view = CandidateDetailsView.as_view()

@api_view(["POST","GET"])
def candidate_list_view(request, *args, **kwargs):
    qs = Candidate.objects.all()
    result_data = CandidateModelSerializer(qs, many = True).data
    
    return Response(data=result_data)

@api_view(["POST","GET"])
def approved_candidate_list_view(request, *args, **kwargs):
    qs = Candidate.objects.all().filter(is_approved = True)
    result_data = CandidateModelSerializer(qs, many = True).data
    
    return Response(data=result_data)


@api_view(["POST","PUT"])
def create_candidate_view(request, *args, **kwargs):
   
    user = User.objects.get(studentNumber = request.data["studentid"])
    data = {
        "student_id": user.studentNumber,
        "name":user.name,
        "surname":user.surname,
        "department": user.department,
        "email":user.email,
        "grade": user.grade
        }
    
    serializer = CandidateModelSerializer(data=data)
    if(serializer.is_valid(raise_exception=True)):
        serializer.save()
        user.hasApplied = True
        user.save()

    candidate = Candidate.objects.get(student_id = user.studentNumber)
    for i in range(1,4):
        file = request.FILES[f"files{i}"]
        if(file):
            document = PDF(file=file, student=candidate)
            document.save()

    return Response(data={
        "status": "added"
    })

@api_view(["POST"])
def candidate_document_view(request, *args, **kwargs):
    studentNumber = request.data["studentid"]
    user = User.objects.get(studentNumber = studentNumber)
    if(user.hasApplied):
        candidate = Candidate.objects.get(student_id = studentNumber)
        qs = PDF.objects.all().filter(student = candidate)
        documents = PDFSerializer(qs,many = True).data
        document_array = []
        print(settings.MEDIA_ROOT)
        for document in documents:
            file_path = unquote(document['file'])
            file_path = os.path.join(settings.MEDIA_ROOT, file_path[1::])
            file = open(file_path, 'rb')
            document_array.append(file)
        response = FileResponse(document_array, as_attachment=True)
        return response
    return Response(data={
        "message": f"The user with student id {studentNumber} has not applied"
    })
