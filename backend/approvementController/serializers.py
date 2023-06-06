from rest_framework import serializers

from candidateController.models import Candidate

class ApprovementSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Candidate
        fields = [
            "student_id",
            "name",
            "is_approved",
            "grade",
            "vote_count",
            "department",
            "is_checked"
        ]
    def get_name(self,obj):
        return obj.name + " " + obj.surname

class ResultSerializer(serializers.ModelSerializer):
    has_most_counts = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Candidate
        fields = [
            "student_id",
            "name",
            "surname",
            "vote_count",
            "is_winner",
            "has_most_counts",
            "grade",
            "department"
        ]
    
    def get_has_most_counts(self,obj):
        candidate_list = Candidate.objects.all().filter(department = obj.department)
        for candidate in candidate_list:
            if(candidate.vote_count > obj.vote_count):
                return False
        return True
