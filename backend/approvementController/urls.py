from django.urls import path

from . import views

urlpatterns = [
    path('resultApprovements/results/department/', views.approvement_list_view, name="Approvement_List_View"),
    path('resultApprovements/results/department/approve/', views.result_approve_view),
    path('resultApprovements/results/department/reject/', views.result_approve_view),
    path('resultApprovements/department/',views.result_list_view, name= "Result_List_View"),
    path('applicationApprovement/application/department/approve', views.application_approve_view, name = "Application_Approve"),
    path('applicationApprovement/application/department/reject', views.application_reject_view, name = "Application_Reject"),
    path('applicationApprovement/application/department/', views.list_application_view, name = "Application_List")
]