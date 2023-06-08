from django.urls import path
from . import views

urlpatterns = [
    path("document/", views.list_document_view, name= "Upload_Document"),
]