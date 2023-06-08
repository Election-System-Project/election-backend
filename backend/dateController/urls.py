from django.urls import path
from . import views

urlpatterns = [
    path('dates/', views.election_list_view),
    path('dates/<int:pk>/', views.election_detail_view),
    path('dates/add/', views.add_dates_view)
]
