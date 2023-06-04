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
                  'electionStatus'
                  ]
    def validate(self, attrs):
        student_number = attrs['studentNumber']
        instance = self.instance  # Get the current instance being updated (if any)

        existing_users = User.objects.filter(studentNumber=student_number).exclude(pk=instance.pk if instance else None)
        if existing_users.exists():
            raise serializers.ValidationError("User with this studentNumber already exists.")
        
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
      