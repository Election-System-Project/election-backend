from django.urls import path
from . import views

urlpatterns = [
    path('dates/', views.election_list_view),
    path('dates/<int:pk>/', views.election_detail_view),
    path('dates/create/', views.election_date_create_view)
]
