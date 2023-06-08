from rest_framework import serializers
from .models import ElectionDate
from datetime import timedelta
import pytz

class ElectionDataSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S%z')
    end_date = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S%z')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tz = pytz.timezone('Etc/GMT+3')
        start_date = instance.start_date.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S%z')
        end_date = instance.end_date.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S%z')
        representation['start_date'] = start_date
        representation['end_date'] = end_date
        return representation

    class Meta:
        model = ElectionDate
        fields = [
            "id",
            "election_type",
            "start_date",
            "end_date"
        ]
        
    def validate(self, data):
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("start date must be less than or equal to end_date")
        all_dates = ElectionDate.objects.all().filter(election_type = "Department")
        if all_dates.exists():
            raise serializers.ValidationError("There is a 'Department' date already")
        if data["election_type"] == "Department" or data["election_type"] == "Faculty":
            return data
        raise serializers.ValidationError("election_type must either be 'Faculty' or 'Department'")