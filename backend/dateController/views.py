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

class ElectionDateListView(generics.ListAPIView):
    queryset = ElectionDate.objects.all()
    serializer_class = ElectionDataSerializer

election_list_view = ElectionDateListView.as_view()

@api_view(["POST"])
def add_dates_view(request,*args,**kwargs):
    print(request.data)
    serializer = ElectionDataSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(data= {
        "Status": "Geldi"
    })