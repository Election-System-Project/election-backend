from rest_framework import generics, mixins

from .models import ElectionDate
from .serializers import ElectionDataSerializer


# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .mixins import (
    StaffEditorPermissionMixin,
    UserQuerySetMixin
)

class ElectionDateCreateView(
    UserQuerySetMixin,
    generics.CreateAPIView,
    StaffEditorPermissionMixin
    ):
    queryset = ElectionDate.objects.all()
    serializer_class = ElectionDataSerializer

election_date_create_view = ElectionDateCreateView.as_view()

class ElectionDateDetailView(generics.RetrieveAPIView):
    queryset = ElectionDate.objects.all()
    serializer_class = ElectionDataSerializer
    lookup_field = 'pk'

election_detail_view = ElectionDateDetailView.as_view()


@api_view(["POST"])
def election_list_view(request, *args, **kwargs):
    qs = ElectionDate.objects.all()
    
    array = []
    for obj in qs:
        new_dict = {
            "electionType":obj.election_type,
            "startDate": obj.start_date,
            "endDate": obj.end_date
        }
        array.append(new_dict)
    
    data = {
        "dates": array
    }
   
    return Response(data=data)

@api_view(["POST"])
def add_dates_view(request,*args,**kwargs):
    print(request.data)
    serializer = ElectionDataSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(data= {
        "Status": "Geldi"
    })

