from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import PDF
from .serializers import PDFSerializer

# Create your views here.
class list_documents(generics.ListAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

list_document_view = list_documents.as_view()