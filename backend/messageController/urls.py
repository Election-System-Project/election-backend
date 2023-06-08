from django.urls import path
from . import views

urlpatterns = [
    path("messages/", views.get_message),
    path("messages/add/", views.add_message),
]