from rest_framework import serializers
from .models import Post, Status

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'status']
        read_only_fields = ['created_at', 'id']
    
    def validate_status(self, value):
        if value not in [choice[0] for choice in Status.choices]:
            raise serializers.ValidationError("Invalid status value.")
        return value