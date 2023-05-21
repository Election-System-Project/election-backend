from django.urls import path
from . import views

urlpatterns = [
    path('announcements/create/', views.announcement_list_create_view, name="create_view"), 
    path('announcements/<int:pk>/',views.announcement_detail_view, name = "detail_view"),
    path('announcements/',views.announcement_list_view, name = "list_view")
]