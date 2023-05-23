from rest_framework import serializers
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'candidate_name', 'count')

    def validate(self, data):
        candidate_name = data.get('candidate_name')
        if not candidate_name:
            raise serializers.ValidationError("Candidate name is required.")
        return data