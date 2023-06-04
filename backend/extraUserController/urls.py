from django.urls import path

from . import views

urlpatterns = [
    path("", view= views.user_list_view, name = "list_user"),
    path("save/", view = views.user_create_view, name = "save_user"),
    path("save/voteStatus/", view=views.user_vote_view, name = "save_vote")
]