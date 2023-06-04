from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PDF,Student
from .serializers import PDFSerializer


@api_view(['POST'])
def upload_pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        description = data['description']
        files = data['files']
        student_id = data['student_id']
        student, created = Student.objects.get_or_create(student_id=student_id)
        for file in files:
            pdf = PDF(name=name, description=description, file=file, student=student)
            pdf.save()
        return JsonResponse({'status': 'success'})


@api_view(['GET'])
def download_pdf(request):
    pdfs = PDF.objects.all()
    pdf_files = []
    for pdf in pdfs:
        pdf_files.append(pdf.file.read())
    response = HttpResponse(pdf_files, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdfs.pdf"'
    return response