from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('',views.create_user_view)
]