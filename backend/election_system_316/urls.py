"""election_system_316 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authcontroller/', include("authcontroller.urls")),
    path('announcementController/', include("announcementController.urls")),
    path('dateController/', include("dateController.urls")),
    path('candidateController/', include("candidateController.urls")),
    path('voteController/', include("voteController.urls")),
    path('approvementController/', include("approvementController.urls")),
    path('userController/', include("extraUserController.urls")),
    path('documentController/', include("documentController.urls")),
    path('messageController/', include("messageController.urls"))
]
