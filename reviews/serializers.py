from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for Review model.
    The user field is read-only and represented as string.
    """
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        """
        Override create method to associate the review with the request user.
        """
        model = Review
        fields = ['id', 'user', 'doctor', 'rating', 'comment', 'timestamp']
        read_only_fields = ['id', 'user', 'timestamp']

    def create(self, validated_data):
        user = self.context['request'].user
        return Review.objects.create(user=user, **validated_data)