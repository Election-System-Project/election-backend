from rest_framework import generics, mixins

from .models import Candidate
from .serializers import CandidateModelSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class CandidateCreateView(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateModelSerializer

candidate_create_view = CandidateCreateView.as_view()


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
