from rest_framework import serializers, fields

from .models import Candidate

class CandidateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            "student_id",
            "name",
            "surname",
            "faculty",
            "department",
            "email",
            "is_approved",
            "grade",
            "is_winner",
            "vote_count"
        ]
    
    def validate(self, attrs):
        if(Candidate.objects.all().filter(student_id=attrs["student_id"]).exists()):
            raise serializers.ValidationError("This id already exists!")
        return attrs