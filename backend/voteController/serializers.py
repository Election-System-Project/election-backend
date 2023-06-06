from rest_framework import serializers
from candidateController.models import Candidate

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['student_id', 'vote_count']

    def validate(self, data):
        candidate_name = data.get('student_id')
        if not candidate_name:
            raise serializers.ValidationError("student_id name is required.")
        return data

