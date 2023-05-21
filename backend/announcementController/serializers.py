from rest_framework import serializers

from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    announceTitle = serializers.SerializerMethodField(read_only = True)
    announceContent = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Announcement
        fields = [
            "id",
            "announceTitle",
            "announceContent",
            "announcement_type"
        ]
    
    def validate(self, data):
        print(data["announcement_type"] == "result")
        if(data["announcement_type"] == "result" or data["announcement_type"] == "general"):
            return data
        raise serializers.ValidationError("announcement_type must be either 'result' or 'general'")
    
    def get_announceTitle(self,obj):
        return obj.title
    
    def get_announceContent(self,obj):
        return obj.content


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            "id",
            "title",
            "content",
            "announcement_type"
        ]
    
    def validate(self, data):
        print(data["announcement_type"] == "result")
        if(data["announcement_type"] == "result" or data["announcement_type"] == "general"):
            return data
        raise serializers.ValidationError("announcement_type must be either 'result' or 'general'")
    

    