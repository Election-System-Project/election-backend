from django.urls import path

from . import views

urlpatterns = [
    path('resultApprovements/results/department/', views.approvement_list_view, name="Approvement_List_View"),
    path('resultApprovements/results/department/approve/', views.result_approve_view),
    path('resultApprovements/results/department/reject/', views.result_approve_view),
    path('resultApprovements/department/',views.result_list_view, name= "Result_List_View")
]