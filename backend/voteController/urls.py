from django.urls import path
from .views import add_vote, get_vote_counts

urlpatterns = [
    path('addvote/', add_vote),
    path('election_status/votes/', get_vote_counts),
]