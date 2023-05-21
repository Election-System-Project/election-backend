from rest_framework import serializers, fields

from .models import ElectionDate

class ElectionDataSerializer(serializers.ModelSerializer):
    start_date = fields.DateField(input_formats=['%Y-%m-%d'])
    end_date = fields.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = ElectionDate
        fields = [
            "id",
            "election_type",
            "start_date",
            "end_date"
        ]
        
    def validate(self, data):
        if(data["start_date"] > data["end_date"]):
            raise serializers.ValidationError("start date must be less than or equal to end_date")
        if(data["election_type"] == "Department" or data["election_type"] == "Faculty"):
            return data
        raise serializers.ValidationError("election_type must either be 'Faculty' or 'Department'")
        

