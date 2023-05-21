from django.urls import path

from . import views

urlpatterns = [
    path("candidates/", views.candidate_list_view),
    path("candidates/<int:pk>/", views.candidate_details_view),
    path("candidates/create/", views.candidate_create_view)
]