from django.urls import path

from . import views

urlpatterns = [
    path("candidates/", views.approved_candidate_list_view, name= "approved_candidates"),
    path("candidates/<int:pk>/", views.candidate_details_view, name = "detail_view"),
    path("candidates/create/", views.candidate_create_view, name = "create_view")
]