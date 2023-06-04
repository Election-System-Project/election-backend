from django.urls import path

from . import views

urlpatterns = [
    path('resultApprovements/', views.result_list_view, name="Aprrovement_List_View"),
    path('resultApprovements/approve/', views.result_approve_view),
    path('resultApprovements/reject/', views.result_approve_view)
]