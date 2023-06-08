from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 
                  'surname', 
                  'studentNumber', 
                  'hasVoted',
                  'hasApplied',
                  'electionStatus',
                  'grade',
                  'email',
                  'department'
                  ]
    def validate(self, attrs):
        
        return attrs
    




class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            'studentNumber',
            'hasVoted' 
            ]
    def validate(self, attrs):
        student_number = attrs.get('studentNumber')
        try:
            user = User.objects.get(studentNumber=student_number)
        except User.DoesNotExist:
            raise serializers.ValidationError("This user does not exist")

        if user.hasVoted:
            raise serializers.ValidationError("This user has already voted")

        return attrs
      