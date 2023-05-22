from rest_framework import generics
from .models import Announcement
from .serializers import AnnouncementSerializer
from .serializers import AnnouncementDetailSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
class AnnouncementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementDetailSerializer

announcement_list_create_view = AnnouncementListCreateAPIView.as_view()

class AnnouncementDetailView(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'pk'

announcement_detail_view = AnnouncementDetailView.as_view()

@api_view(["GET", "POST"])
def announcement_list_view(request, *args, **kwargs):
    result_data = {}
    general_data = {}
    qs = Announcement.objects.all().filter(announcement_type = "result")
    if qs:
        result_data = AnnouncementSerializer(qs, many = True).data
    qs = Announcement.objects.all().filter(announcement_type = "general")
    if qs:
        general_data = AnnouncementSerializer(qs, many=True).data
    general_data = { 
        "title": "General Announcements",
        "announcementList": general_data
    }
    result_data = { 
        "title": "Result Announcements",
        "announcementList": result_data
    }
    data = {"array":[
        general_data,
        result_data
    ]}
    return Response(data=data)
